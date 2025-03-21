import asyncio
import re
from global_settings import *
import edge_tts
import pyttsx3
engine = pyttsx3.init()

VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "outputs/tts.mp3"

async def pts(a):
    engine.save_to_file(a, "outputs/tts.mp3")
    engine.runAndWait()


async def generate(a):
    communicate = edge_tts.Communicate(a, VOICE, rate="+56%")
    await communicate.save(OUTPUT_FILE)

async def createTtsOfTitle(a):
    communicate = edge_tts.Communicate(a, VOICE, rate="+56%")
    await communicate.save("outputs/titleTts.mp3")

async def edgeTtsGen(a):
    communicate = edge_tts.Communicate(a, VOICE, rate="+70%")
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_FILE, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)

    srt_text = submaker.get_srt()
    segments = []
    lines = srt_text.strip().split('\n')
    i = 0
    while i < len(lines):
        if lines[i].isdigit():
            start, end = lines[i + 1].split(' --> ')
            start_time = srt_time_to_seconds(start)
            end_time = srt_time_to_seconds(end)
            text = lines[i + 2] if i + 2 < len(lines) else ''
            
            segments.append({
                "start": start_time,
                "end": end_time,
                "words": [{"text": word, "start": start_time, "end": end_time} for word in text.split()]
            })
            i += 3
        else:
            i += 1
    return {"segments": segments}

def srt_time_to_seconds(srt_time):
    time_parts = re.split('[:,]', srt_time)
    h, m, s, ms = map(int, time_parts)
    return h * 3600 + m * 60 + s + ms / 1000.0