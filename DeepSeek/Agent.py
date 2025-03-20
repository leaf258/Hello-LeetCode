import json
from pathlib import Path
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults

config_path = Path("DeepSeek\config.json")
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

# 初始化模型和工具
llm = ChatOpenAI(    
    openai_api_key=config["openai_api_key"],
    base_url=config["base_url"],
    model="deepseek-chat"
    )
search = DuckDuckGoSearchResults()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for answering questions about current events."
    )
]

# 创建 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 执行任务
result = agent.invoke("What's the latest news about AI?")
print(result["output"])