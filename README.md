# Youtube Shorts Generator Thing
## by nanop :D

The ultimate retarded way to make youtube shorts with minecraft parkour (or anything really) in the background

## Installation
I can call this done i think

This uses groq for the ai processing (potentially even ollama for local ai processing for more freedom), edge-tts for the tts and transcript, and moviepy to edit everything together. God help me.

Its highly recommended for you to create this in a virtual python environment (py -m venv "your proj") because of organization stuff, some packages could conflict with other versions of the same packages, its just- it uses specific versions, and if you have another version of that same package already installed it might not work. Just trust me.

### ./res folder
This folder includes all background stuff, including background videos, background music, etc. This wont be in the github, although i could create a google drive link for all the videos if you do want it. If you dont, you could totally just recreate the res folder yourself with your own data. It doesnt really matter, it picks randomly.

The res folder:
```
res/
├─ bg_videos/
├─ bg_music/

```

### ./output folder
this probably got deleted but if you do decide to use this then make sure to create this directory

### ./groqKey.py
this is a file that returns the key. Not included for obvious reasons, but all you have to do is create a file with this script
``` py
def get():
    return "yOurgrOqAIkEyHereLOl"
```

# LOG
## #0

I initially wanted to use whisper-timestamped transcribing because at first i wanted flexibility over ai voices, but edge-tts seemed to work best. edge-tts also came with its own subtitling engine, so i basically wrote a translator type thing that translates srt files (the edgetts subtitle output) to ones readable by the already existing in movie.py. Why dont i just update the code
entirely?? edge-tts seems like one of those too good to be true type occurances, where you KNOW microsoft is gonna find out and absolutely demolish it, Therefore i wont be adding full,
deep support to edge-tts. This is why all functions are modular in the first place, one of these could fail and it wont bring down the entire thing.

TLDR: I was dumb and didnt realize edge-tts had a built in subtitle creator.

## #1 (3/19/25)

I can maybe call it done, its at a point where i can sit at the terminal and run the program, type out a prompt and hope the ai doesnt generate too long of a script, then just wait maybe 2 or 3 minutes. If you want to try this out go ahead but i am warning you that i mostly made this for shits and giggles (and to throw shade at that one site that almost tricked me into paying just to generate brainrot shorts, i just stole their entire idea lmao)

Currently the system prompt is more focused on reddit AITA stories, but you can easily just replace that by editing system_message in aiFunctions. Again, i just made this for myself, i didnt
really think of anything to make this user friendly lollll

last thing, when the script becomes too long, as long as your background videos are longer than the script it wont tweak out
