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

async def main():
    global TITLE
    global AISCRIPT
    global RETTRANS

    aiInput = input("Generate any idea. >")
    print("Okay! Ai will begin process now. You have brought this upon yourself.")
    
    getFromAi = Spinner()
    with getFromAi:
        print(" Waiting for response from ai...")
        RAWAISCRIPT = await af.get(aiInput)
        
        TITLE = json.loads(RAWAISCRIPT)["title"]
        AISCRIPT = TITLE + json.loads(RAWAISCRIPT)["text"]
        print(TITLE)
        print ("Ai has returned this script based on your input:")
        print(AISCRIPT);
        
    generateTts = Spinner()
    with generateTts:
        print(" Waiting for tts...")
        if(OFFLINE_MODE):
            await tf.pts(AISCRIPT)
        if(USES_EDGETTS):
            await tf.createTtsOfTitle(TITLE)
            RETTRANS = await tf.edgeTtsGen(AISCRIPT)
        else:
            await tf.generate(AISCRIPT)
    generateTranscript = Spinner()
    with generateTranscript:
        if(OFFLINE_MODE and not USES_EDGETTS):
            print(" Waiting for transcript...")
            RETTRANS = await trf.doTranscribe()
            pausing = input("This pause is to give you extra time to fix the ai-transcript, because its extremely buggy. Press anything to continue >")
    generateMovie = Spinner()
    with generateMovie:
        tc.createCard(TITLE)
        await mv.magic(RETTRANS)
    print("...")
    print("...")
    print("FINISHED!")
    
    

asyncio.run(main())