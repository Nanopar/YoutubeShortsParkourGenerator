import asyncio
import groqKey as gk #Add a python file in the root directory named this, make a function get() that returns the key. For obvious reasons i dont have this included.
import re
from global_settings import  *

system_message = """write a AM I THE ASSHOLE (AITA) reddit story for any topic the user asks for. remove the starting \"Title:\" just go straight to the title. make it decently sized, not too long, if it were a video it would be under a minute. if necessary for the story, add the (ageGENDER) where gender is F or M when referring to people, yes the parenthesis is important. You use this when introducing the characters. Avoid using \"—\" and * as it messes with the tts, consider using commas instead. Try not to accidentally type chinese."""

async def get(a) -> str:
    if(OFFLINE_MODE):
        from ollama import AsyncClient
        message = {'role': 'user', 'content': a}
        response = await AsyncClient().chat(model='llama3.2', messages=[{'role': 'system', 'content': system_message} ,message])
        #print(response.message.content)
        return response.message.content
    else:
        from groq import Groq
        client = Groq(api_key=gk.get())
        completion = client.chat.completions.create(
            model="qwen-qwq-32b",
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": a
                },
            ],
            temperature=0.6,
            max_completion_tokens=1024,
            top_p=0.95,
            stop=None,
        )
        frmt = re.sub(r"<think>.*?</think>", "", completion.choices[0].message.content, flags=re.DOTALL).strip()
        #print(frmt)
        return frmt