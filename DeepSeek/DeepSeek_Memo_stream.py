import json
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 配置流式回调处理器
class CustomStreamHandler(StreamingStdOutCallbackHandler):
    def __init__(self):
        super().__init__()
        self.content = ""
    
    def on_llm_new_token(self, token: str, **kwargs):
        # 实时输出每个token
        print(token, end="", flush=True)
        self.content += token

config_path = Path("DeepSeek\config.json")
with open(config_path, 'r', encoding='utf-8') as f: # 上下文管理功能
    config = json.load(f)


# 配置支持流式的Chat模型 # deepseek-chat 模型对应 DeepSeek-V3；deepseek-reasoner 模型对应 DeepSeek-R1。
chat = ChatOpenAI(
    openai_api_key=config["openai_api_key"],
    base_url=config["base_url"],
    model="deepseek-chat", # model="deepseek-chat", 需要构建聊天机器人、处理开放式话题讨论、生成创意文案/故事   # model="deepseek-reasoner",解决数学/物理问题、生成复杂代码逻辑、需要分步骤解释的推理任务
    streaming=True,  # 启用流式模式
    callbacks=[CustomStreamHandler()]  # 添加自定义流处理器
)

# 创建带记忆的对话链
memory = ConversationBufferMemory(
    max_token_limit=500,  # 保留最近500token的对话
    return_messages=True
)
conversation = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=False
)

def main():
    print("开始对话（输入 'exit' 退出）")
    while True:
        user_input = input("\n用户: ")
        
        if user_input.lower() == 'exit':
            print("对话结束")
            break
            
        # 创建新的流处理器实例
        stream_handler = CustomStreamHandler()
        
        # 带流式处理的对话调用
        print("\nAI: ", end="", flush=True)
        # 异常处理增强
        try:
            response = conversation.invoke(
                input=user_input,
                callbacks=[stream_handler]  # 为本次调用附加处理器
            )
        except Exception as error:
            print(f"\n发生错误: {str(error)}")
            memory.chat_memory.add_ai_message("[对话异常中断]")
        
        # 将完整响应存入记忆
        memory.save_context(
            {"input": user_input}, 
            {"output": stream_handler.content}
        )
        
        # 清空当前内容
        stream_handler.content = ""

if __name__ == "__main__":
    main()