import os
from dotenv import load_dotenv 
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio


load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client= external_client
)


config = RunConfig(
    model= model,
    model_provider=external_client,
    tracing_disabled = True
)


async def main():
    
    agent = Agent(
        name="helloWorld",
        instructions= "you are a hello world agent, who just responses in hello world, with the response(actual answer) shortly",
        model=model,
    )
    
    
    response = await Runner.run(agent, "tell me about recursion", run_config=config)
    
    print(response.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())     