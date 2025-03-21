# libraries Import
import threading
from tkinter import *
import customtkinter
import asyncio
import json
from utils.Spinner import Spinner
import functions.aiFunctions as af
import functions.ttsFunctions as tf
import functions.transcribeFunctions as trf
import moviemagic.movie as mv
import moviemagic.createTitleCard as tc
from global_settings import *

TITLE = """"""
AISCRIPT = """"""
RETTRANS = """"""

window = Tk()
window.title("Generator GUI")
window.geometry("480x480")
window.configure(bg="#151515")


notice = customtkinter.CTkLabel(
    master=window,
    text="IDLE...",
    font=("Arial", 12),
    text_color="#ffffff",
    height=30,
    width=438,
    corner_radius=4,
    bg_color="#151515",
    fg_color="#111111",
    )
notice.place(x=20, y=440)
Label_aad5 = customtkinter.CTkLabel(
    master=window,
    text="^^YOU CAN GENERATE OR MAKE ONE YOURSELF^^",
    font=("Arial", 12),
    text_color="#ffffff",
    height=30,
    width=438,
    corner_radius=4,
    bg_color="#151515",
    fg_color="#111111",
    )
Label_aad5.place(x=20, y=370)
genVid = customtkinter.CTkButton(
    master=window,
    text="Generate Video",
    font=("undefined", 14),
    text_color="#ffffff",
    hover=True,
    hover_color="#5f5f5f",
    height=30,
    width=116,
    border_width=2,
    corner_radius=6,
    border_color="#c0c0c0",
    bg_color="#151515",
    fg_color="#4f4f4f",
    )
genVid.place(x=180, y=400)
genScript = customtkinter.CTkButton(
    master=window,
    text="Generate Script",
    font=("undefined", 14),
    text_color="#ffffff",
    hover=True,
    hover_color="#5f5f5f",
    height=30,
    width=116,
    border_width=2,
    corner_radius=6,
    border_color="#c0c0c0",
    bg_color="#151515",
    fg_color="#4f4f4f",
    )
genScript.place(x=340, y=30)
script = customtkinter.CTkTextbox(
    master=window,
    #placeholder_text="Ai generated script will go here...",
    #placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#ffffff",
    
    height=291,
    width=438,
    border_width=2,
    corner_radius=6,
    border_color="#4e4e4e",
    bg_color="#151515",
    fg_color="#333333",
    )
script.place(x=20, y=70)
genTitle = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Type a title or an idea",
    placeholder_text_color="#606060",
    font=("Arial", 14),
    text_color="#ffffff",
    height=30,
    width=320,
    border_width=2,
    corner_radius=6,
    border_color="#4f4f4f",
    bg_color="#151515",
    fg_color="#333333",
    )
genTitle.place(x=20, y=30)


def generateScript():
    async def inner():
        notice.configure(text="generating script...")
        notice.configure(text="generating script...")
        notice.configure(text="generating script...")
        RAWAISCRIPT = await af.get(genTitle.get())
        TITLE = json.loads(RAWAISCRIPT)["title"]
        AISCRIPT = TITLE + json.loads(RAWAISCRIPT)["text"]
        genTitle.delete(0,"end")
        genTitle.insert(0, TITLE)
        script.insert("1.0", AISCRIPT)


        print(TITLE)
        print ("Ai has returned this script based on your input:")
        print(AISCRIPT);
    asyncio.run(inner())
def startGenerationProcess():
    async def binner():
        ##TTS
        notice.configure(text="Generating TTS...")
        print(" Waiting for tts...")
        if(OFFLINE_MODE):
            await tf.pts(script.get("0.0","end"))
        if(USES_EDGETTS):
            await tf.createTtsOfTitle(genTitle.get())
            RETTRANS = await tf.edgeTtsGen(script.get("0.0","end"))
        else:
            await tf.generate(script.get("0.0","end"))
        
        ##Transcript (If not edgetts)
        if(OFFLINE_MODE and not USES_EDGETTS):
            notice.configure(text="Generating AI Transcript...")
            print(" Waiting for transcript...")
            RETTRANS = await trf.doTranscribe()
            pausing = input("This pause is to give you extra time to fix the ai-transcript, because its extremely buggy. Press anything to continue >")
        
        ##Movie generation
        notice.configure(text="generating youtube short...")
        tc.createCard(genTitle.get())
        await mv.magic(RETTRANS)
        notice.configure(text="Done! it's inside outputs/final.mp4")
    def startRun():
        asyncio.run(binner())
    
    genThread = threading.Thread(target=startRun)
    genThread.start()
    
        
genScript._command = generateScript
genVid._command = startGenerationProcess

window.mainloop()
