import pyttsx3


engine = pyttsx3.init()

VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "outputs/tts.mp3"

engine.save_to_file("""Did you know?
if youre watching this youre sigma""", "outputs/tts.mp3")
