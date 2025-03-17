import asyncio
import edge_tts
VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "outputs/tts.mp3"
async def generate(a):
    communicate = edge_tts.Communicate(a, VOICE, rate="+50%")
    await communicate.save(OUTPUT_FILE)
    