import json
from pathlib import Path
from openai import OpenAI

config_path = Path("DeepSeek\config.json")
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

client = OpenAI(
    api_key=config["openai_api_key"],
    base_url=config["base_url"]
)


def process_input(user_input:str):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content":user_input},
        ],
        stream=False
    )
    return response


def main():
    # 提示用户输入
    user_input = input("用户输入: ")
    
    # 处理输入
    response = process_input(user_input)
    
    # 输出结果
    print(response.choices[0].message.content)
 
if __name__ == "__main__":
    main()

