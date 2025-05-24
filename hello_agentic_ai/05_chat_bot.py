import os
from dotenv import load_dotenv
from agents import Runner,Agent,AsyncOpenAI,OpenAIChatCompletionsModel
from agents.run import RunConfig
import chainlit as cl
import asyncio

load_dotenv()

Gemini_api_key = os.getenv("GEMINI_API_KEY")



external_client = AsyncOpenAI(
    api_key = Gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

agent = Agent(
    name= "lalantap",
    instructions= "UR Fucking agent u only know math simple operations",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client = external_client
    )
)



async def chatBot():
    @cl.on_chat_start
    async def chalbhi():

        cl.user_session.set("chat_history", [])


        await cl.Message(content ="hey man how are u").send()
        
    @cl.on_message
    async def quest(msg:cl.message):
        
        
        chat_history = cl.user_session.get("chat_history")
        
        chat_history.appen({"role": "user", "message": msg.content})
        
        
        try:        
            
            response = Runner.run_sync(starting_agent = agent, input=chat_history)
            output = response.final_output
        except Exception as e:
            await cl.Message(content= e).send()
            
            
        await cl.Message(content= output).send()
        
asyncio.run(chatBot())
        
        