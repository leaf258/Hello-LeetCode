import json
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


config_path = Path("DeepSeek\config.json")
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

# 注意：这里使用LangChain的ChatOpenAI封装（而非原生OpenAI客户端）
chat = ChatOpenAI(
    openai_api_key=config["openai_api_key"],
    base_url=config["base_url"],
    model="deepseek-chat"
)

# 创建带记忆的对话链
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=False  # 设为True可以看到详细交互过程
)

def main():
    print("开始对话（输入 'exit' 退出）")
    while True:
        user_input = input("用户: ")
        
        if user_input.lower() == 'exit':
            print("对话结束")
            break
            
        # 通过对话链处理带上下文的请求
        response = conversation.invoke({"input": user_input})
        
        print(f"\nAI: {response['response']}\n")

if __name__ == "__main__":
    main()