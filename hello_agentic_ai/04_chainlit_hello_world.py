import chainlit as cl




@cl.on_message
async def hello_world(message: cl.message):
    
    
    await cl.Message(
        content = f"you said: {message.content}"
    ).send()