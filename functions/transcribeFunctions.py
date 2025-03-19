import json
from global_settings import *

async def doTranscribe():
    import whisper_timestamped as whisper
    if(OFFLINE_MODE and not USES_EDGETTS):
        audio = whisper.load_audio("outputs/tts.mp3")
        model = whisper.load_model("tiny", device="cpu")
        result = whisper.transcribe(model, audio, language="en")
        #fRes = json.dumps(result, indent = 2, ensure_ascii = False)
        fRes = result
        return(fRes)
    