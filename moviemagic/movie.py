import random
from moviepy import *
import moviepy.audio.fx as afx
import numpy as np
import os
from global_settings import *


def pop_effect(t):
    return max(0.6, min(1, t / 0.05))

def zoom_effect(t):
    return (t+40)*0.025

async def magic(data):
    
    randomBgVideoList = os.listdir("res/bg_videos/")
    randomBgMusicList = os.listdir("res/bg_music/")
    
    clip = VideoFileClip(f"res/bg_videos/{random.choice(randomBgVideoList)}")
    ttsClip = AudioFileClip("outputs/tts.mp3")
    bgMusic = AudioFileClip(f"res/bg_music/{random.choice(randomBgMusicList)}")
    bgMusic = bgMusic.with_volume_scaled(0.07)
    bgMusic = bgMusic.with_effects([afx.AudioLoop(duration=ttsClip.duration)])
    mixedAudio = CompositeAudioClip([ttsClip, bgMusic])
    clip = clip.subclipped(0, ttsClip.duration)
    clip.audio = mixedAudio
    text_clips = []
    
    ttsTitleCard = AudioFileClip("outputs/titleTts.mp3")
    titleCardClip = ImageClip("outputs/titleCard.png", False, True, False, ttsTitleCard.duration - 0.25).resized(lambda t: zoom_effect(t))
    titleCardClip = titleCardClip.with_position("center")
    
    for segment in data["segments"]:
        for word in segment["words"]:
            text_clip = TextClip(
                text=word["text"],
                font="DEFAULT.TTF",
                font_size = 100,
                color="white",
                stroke_width=12,
                stroke_color="black",
            ).with_position(("center", "center")).with_start(word["start"]).with_duration(word["end"] - word["start"]).resized(lambda t: pop_effect(t))
            text_clips.append(text_clip)
    
    wm = ImageClip("watermark.png", transparent=True)
    
    wm = wm.with_opacity(0.25)
    wm = wm.with_position("center")
    wm = wm.with_duration(clip.duration)
    
    final_clip = CompositeVideoClip([clip, wm] + text_clips + [titleCardClip])
    final_clip.write_videofile("outputs/final.mp4", codec="libx264", audio_codec="aac", fps=24, threads=4)