import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
    openai_client = external_client
)

config = RunConfig(
    model=model,
    model_provider = external_client,
    tracing_disabled = True
    
)



def main():
    agent = Agent(
        name= "khatarnak",
        instructions= "you are a khatarnak agents, which will answer the user."
    )
    
    
    response = Runner.run_sync(agent, "what is your name buddy?", run_config= config)
    
    print(response.final_output)



if __name__== "__main__":
    main()