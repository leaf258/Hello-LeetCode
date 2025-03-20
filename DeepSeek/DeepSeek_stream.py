import json
from pathlib import Path
from openai import OpenAI

config_path = Path("DeepSeek\config.json")
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

client = OpenAI(
    api_key=config["openai_api_key"],
    base_url=config["base_url"],
)


def process_input(user_input: str):
    # 开启流式传输
    stream = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input},
        ],
        stream=True  # 启用流式模式
    )
    return stream

def main():
    user_input = input("用户输入: ")
    
    # 获取流式响应对象
    stream = process_input(user_input)
    
    print("\nAI 回复：", end="", flush=True)
    full_response = []
    
    # 逐块处理响应
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)  # 逐字符打印
            full_response.append(content)
    
    # 最终换行并保留完整响应
    print("\n")
    return "".join(full_response)

if __name__ == "__main__":
    main()