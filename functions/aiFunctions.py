import asyncio
import groqKey as gk #Add a python file in the root directory named this, make a function get() that returns the key. For obvious reasons i dont have this included.
import re
from global_settings import  *

system_message = """write an AM I THE ASSHOLE (replace all AITA mentions with am i the asshole as it messes with the tts) reddit story for any topic the user asks for, and make it interesting and something worth watching, not just a boring story. ALWAYS OUTPUT IN THIS FORMAT {"title":"title","text":"text"} MAKE IT A VALID JSON. Make the title ask a question that the post answers, like "what is the most annoying thing your partner has done?" or "What is the best thing that has happened to you unintentionally?" things like that. Make the title short. Make the actual script decently sized, not too long, if it were a video it would be under a minute. If necessary for the story, add the (ageGENDER) where gender is F or M when referring to people, yes the parenthesis is important. You use this when introducing the characters. Avoid using \"—\", * and \n as it messes with the tts, consider using commas instead. Try not to accidentally type chinese."""

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