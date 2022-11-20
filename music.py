# -*- coding: UTF-8 -*-
from moviepy.editor import *
import os
from random import choice

file_path = './music/'

music_list = []

for f in os.listdir(file_path):
    music_list.append(file_path + f)


def music_clip(dur):
    audio_clip = AudioFileClip(choice(music_list))
    return audio_clip.set_duration(dur)
