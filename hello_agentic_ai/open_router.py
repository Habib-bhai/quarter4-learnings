import asyncio
import os
from dotenv import load_dotenv
# import requests 
# import json
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai import AsyncOpenAI

load_dotenv()
# Load environment variables

# OPENROUTER_API_KEY = os.getenv("OPEN_ROUTER_KEY")

# set_tracing_disabled(disabled=True)
# BASE_URL = "https://openrouter.ai/api/v1"
# MODEL = "deepseek/deepseek-prover-v2:free"


# response = requests.post(
#     url=f"https://openrouter.ai/api/v1/chat/completions",
#     headers={
#     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#     },
#     data=json.dumps({
#     "model": MODEL,
#     "messages": [
#       {
#         "role": "user",
#         "content": "Hi, i have 1000 pkr i want you to convert into usd"
#       }
#     ]
#   })
# )


# print(response.json().get("choices")[0].get("message").get("content"))



CLIENT = AsyncOpenAI(
    api_key = OPENROUTER_API_KEY,
    base_url = BASE_URL 
)


async def main():
    agent = Agent(
        name="khatarnakAgent",
        instructions="you are a khatarnak agent who replied with sarcasm",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=CLIENT)
    )
    
    response = await Runner.run(agent, "What is your name? show your abilities")
    
    print(response.final_output)
    
    
if __name__ == "__main__":
    asyncio.run(main())    