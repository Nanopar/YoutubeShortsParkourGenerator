# Youtube Shorts Generator Thing
## by nanop :D

The ultimate retarded way to make youtube shorts with minecraft parkour in the background

## Installation
This isnt even done yet. Dont attempt to fork and build it yourself, its really incomplete.

This will use groq for the ai processing (potentially even ollama for local ai processing for more freedom), edge-tts for the tts, whisper-timestamped for the subtitle transcript, and moviepy to edit everything together. God help me.

Its highly recommended for you to create this in a virtual python environment (py -m venv "your proj") because of organization stuff, some packages could conflict with other versions of the same packages, its just- it uses specific versions, and if you have another version of that same package already installed it might not work. Just trust me.

## ./res folder
This folder includes all background stuff, including background videos, background music, etc. This wont be in the github, although i could create a google drive link for all the videos if you do want it. If you dont, you could totally just recreate the res folder yourself with your own data. It doesnt really matter, it picks randomly.