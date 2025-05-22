from agents import Agent, ModelSettings, function_tool, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# this decorator will help us define the tools, the agent can use to achieve its tasks.
@function_tool
def sum(a: int, b: int):
    return a + b


client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


async def main():
    agent  = Agent(
        name="joker",
        instructions="You are a funny assistant. You only respond in jokes.",
        model= OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client) ,
    )


    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

    print(result.final_output)
    
    
if __name__ == "__main__":
    asyncio.run(main())