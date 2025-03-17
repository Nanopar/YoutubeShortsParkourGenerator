import asyncio
from utils.Spinner import Spinner
import functions.aiFunctions as af
import functions.ttsFunctions as tf
import functions.transcribeFunctions as trf
import moviemagic.movie as mv
AISCRIPT = """"""
RETTRANS = """"""
async def main():
    global AISCRIPT
    global RETTRANS
    
    aiInput = input("Generate any idea. >")
    print("Okay! Ai will begin process now. You have brought this upon yourself.")
    
    getFromAi = Spinner()
    with getFromAi:
        print(" Waiting response from ai...")
        AISCRIPT = await af.get(aiInput)
        print ("Ai has returned this script based on your input:")
        print(AISCRIPT);
        
    generateTts = Spinner()
    with generateTts:
        print(" Waiting tts from edge-tts...")
        await tf.generate(AISCRIPT)
    generateTranscript = Spinner()
    with generateTranscript:
        print(" Waiting transcript from whisper...")
        RETTRANS = await trf.doTranscribe()
    pausing = input("This pause is to give you extra time to fix the ai-transcript, because its extremely buggy. Press anything to continue >")
    generateMovie = Spinner()
    with generateMovie:
        await mv.magic(RETTRANS)

    print("...")
    print("...")
    print("FINISHED!")
    
    nextStep = input("Try again? y/n >")
    if(nextStep == "y"):
        asyncio.run(main())
    else:
        exit()
    

asyncio.run(main())