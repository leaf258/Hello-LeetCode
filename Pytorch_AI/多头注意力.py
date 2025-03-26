import math
import torch
import torch.nn as nn
from labml_nn.utils import clone_module_list
from labml_nn.transformers.feed_forward import FeedForward
from labml_nn.transformers.mha import MultiHeadAttention
from labml_nn.transformers.positional_encoding import get_positional_encoding

## 嵌入 token 并添加固定位置编码
class EmbeddingsWithPositionalEncoding(nn.Module):
    def __init__(self, d_model:int, n_vocab:int, max_len:int=5000):
        super().__init__()
        self.linear = nn.Embedding(n_vocab, d_model) # 创建一个词嵌入层，将词汇表中的每个词（共 n_vocab 个）映射为 d_model 维的向量。
        self.d_model = d_model
        self.register_buffer('positional_encodings', get_positional_encoding(d_model, max_len)) # register_buffer 将位置编码张量注册为缓冲区 (buffer)，使其随模型移动到 CPU/GPU、不参与梯度计算（固定值，无需训练）、随模型保存/加载
        # get_positional_encoding(d_model, max_len)生成形状为 (max_len, d_model) 的位置编码矩阵（通常使用正弦和余弦函数生成）。

    def forward(self, x:torch.Tensor):
        pe = self.positional_encodings[:x.shape[0]].requires_grad_(False) # self.positional_encodings[:x.shape[0]] 根据输入序列长度 x.shape[0]（假设输入为 (seq_len, batch_size)），截取前 seq_len 个位置编码，通过广播机制与词嵌入相加。；requires_grad_(False) 显式禁止位置编码参与梯度计算（虽然 register_buffer 已默认不计算梯度，但显式声明更安全）。
        return self.linear(x) * math.sqrt(self.d_model) + pe # self.linear(x) * math.sqrt(self.d_model) 对词嵌入结果进行缩放。目的是在后续与位置编码相加时，保持数值稳定性（避免梯度消失/爆炸）。
    
## 嵌入 token 并添加参数化的位置编码
class EmbeddingsWithLearnedPositionalEncoding(nn.Module): # 结合词嵌入 (Word Embedding) 和可学习位置编码 (Learned Positional Encoding) ,位置编码是通过训练自动学习的参数，适用于需要动态调整位置信息的场景
    def __init__(self, d_model:int, n_vocab:int, max_len:int=5000): # max_len的设置是为了处理不同长度的序列,此代码会截取前 max_len 个位置编码。若需处理更长的序列，需调整 max_len 或动态扩展位置编码（如插值）。
        super().__init__()
        self.linear = nn.Embedding(n_vocab, d_model) # 词嵌入层
        self.d_model = d_model # 嵌入维度
        self.positional_encodings = nn.Parameter(torch.zeros(max_len, 1, d_model), requires_grad=True) # nn.Parameter 将位置编码定义为可训练参数; 形状：(max_len, 1, d_model)，其中 1 是占位符，便于后续广播到批次维度。;​初始化：初始化为全零张量（通过训练逐步调整）。;requires_grad=True：允许梯度计算，优化器会更新此参数
    
    def forward(self, x:torch.Tensor):
        pe = self.positional_encodings[:x.shape[0]] # 截取当前序列长度的位置编码; 根据输入序列长度 x.shape[0]（假设输入形状为 (seq_len, batch_size)）截取前 seq_len 个位置编码。; ​形状：(seq_len, 1, d_model); ​广播机制：与词嵌入结果相加时，自动扩展为 (seq_len, batch_size, d_model)，确保每个批次中的样本共享相同的位置编码。
        return self.linear(x) * math.sqrt(self.d_model) + pe
    
## Transformer Layer 这可以作为编码器层或解码器层。我们使用预正则化。
class TransformerLayer(nn.Module):
    def __init__(self, *, # 这里的*号用于强制后面的参数必须以关键字形式传递，而不能按位置传递。这通常用于提高代码的可读性和避免参数顺序错误。
                 d_model:int, 
                 self_attn:MultiHeadAttention, # 模块初始化（__init__方法）:当创建MultiHeadAttention实例时（例如在TransformerLayer的__init__中），通过self_attn = MultiHeadAttention(...)传入结构参数（如头数num_heads、模型维度d_model等）
                 src_attn:MultiHeadAttention=None, # 可选的“源注意力”层，用于处理来自另一个序列的注意力（例如解码器中关注编码器输出的注意力）。在编码器层中通常为 None，仅在解码器层中需要。
                 feed_forward:FeedForward,
                 dropout_prob:float):
        super().__init__()
        self.size = d_model
        self.self_attn = self_attn
        self.src_attn = src_attn # 保存传入的源注意力层（如果存在）
        self.feed_forward = feed_forward
        self.dropout = nn.Dropout(dropout_prob)
        self.norm_self_attn = nn.LayerNorm([d_model]) # 为自注意力层的输出定义层归一化（Layer Normalization）
        if self.src_attn is not None:
            self.norm_src_attn = nn.LayerNorm([d_model]) # 如果存在源注意力层，则为其输出定义层归一化。
        self.norm_ff = nn.LayerNorm([d_model]) # 为前馈网络输出定义层归一化
        self.is_save_ff_input = False # 是否将输入保存到前馈层

    def forward(self, *, 
                x:torch.Tensor, 
                mask:torch.Tensor,
                src:torch.Tensor = None, # 源序列，可能来自编码器输出
                src_mask:torch.Tensor = None):
        # 自注意力
        z = self.norm_self_attn(x) # 对输入x进行层归一化，这里的norm_self_attn是在初始化时定义的LayerNorm层
        self_attn = self.self_attn(query=z, key=z, value=z, mask=mask) # MultiHeadAttention类的forward方法设计为接受这些参数
        # PyTorch约定：直接调用模块实例（如self.self_attn(...)）会自动调用其forward方法，无需显式写.forward()。在调用self.self_attn(query=z, key=z, value=z, mask=mask)时，实际触发的是MultiHeadAttention的forward方法。
        x = x + self.dropout(self_attn) #  残差连接：将原始输入x与经过dropout的自注意力输出相加，实现残差结构
        # 源数据
        if src is not None: # 如果存在源序列 src（解码器需要处理编码器输出时），执行交叉注意力
            z = self.norm_src_attn(x) # 对上一步得到的x进行层归一化，使用专门为源注意力准备的LayerNorm层,（Pre-LN 结构，先归一化再进入子层）
            attn_src = self.src_attn(query=z, key=src, value=src, mask=src_mask) # 这里调用src_attn层，query是当前处理后的z，而key和value来自src（编码器输出），mask是src_mask
            x = x + self.dropout(attn_src) # 同样残差连接，将源注意力输出加入x
        # 前馈
        z = self.norm_ff(x) #  对当前的x进行层归一化，用于前馈网络。
        if self.is_save_ff_input:
            self.ff_input = z.clone() #  如果设置了保存前馈网络输入，则克隆z到ff_input属性，可能用于调试或可视化
        ff = self.feed_forward(z) # 将归一化后的z输入前馈网络
        x = x + self.dropout(ff) # 残差连接，将前馈网络的输出加入x
        return x
    
## Transformer 编码器
class Encoder(nn.Module):
    def __init__(self, layer:TransformerLayer, n_layers:int):
        super().__init__()
        self.layers = clone_module_list(layer, n_layers)
        self.norm = nn.LayerNorm([layer.size])  # 添加最终的层归一化

    def forward(self, x:torch.Tensor, mask:torch.Tensor=None):
        """
        前向传播
        :param x: 输入张量，形状为 [seq_len, batch_size, d_model]
        :param mask: 注意力掩码，形状为 [seq_len, seq_len, batch_size]
        :return: 编码器输出，形状为 [seq_len, batch_size, d_model]
        """
        # 依次通过每个 Transformer 层
        for layer in self.layers:
            x = layer(x=x, mask=mask)
        
        # 最终的层归一化
        return self.norm(x)

## Transformer 解码器
class Decoder(nn.Module):
    def __init__(self, layer:TransformerLayer, n_layers:int):
        super().__init__()
        self.layers = clone_module_list(layer, n_layers)

## 生成器


## 组合编码器-解码器