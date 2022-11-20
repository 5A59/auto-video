# -*- coding: UTF-8 -*-
import datetime
from random import sample

from moviepy.editor import *

import numpy as np
from moviepy.editor import *


# WE CREATE THE TEXT THAT IS GOING TO MOVE, WE CENTER IT.


def clip_typewriter(text_list, duration_clip, duration_effect, screensize):
    # `duration_effect` is effectively the time where the last letter appears.
    # letters = findObjects(clip_text, preview=False)
    clips_letters = []
    all_len = 0
    max_len = 0
    for text in text_list:
        all_len += len(text)
        max_len = max(max_len, len(text))

    tmp_duration = duration_effect
    times_start = [tmp_duration * i / (all_len - 1) for i in range(all_len)]
    text_index = 0
    fontsize = 90
    divider = 30

    start_x = (screensize[0] - max_len * fontsize) / 2
    start_y = 600
    for index, text in enumerate(text_list):
        letters = list(text)
        # Select the start time in seconds for each letter found:
        n = len(letters)
        for i, letter in enumerate(letters):
            clip_text = TextClip(
                letter,
                color='black',
                font='方正粗黑宋简体',
                # font='simhei',
                fontsize=fontsize,
                kerning=3,
            )
            clips_letters.append(clip_text
                                 .set_position((i * fontsize + start_x, start_y + index * fontsize + divider * index))
                                 .set_start(times_start[text_index])
                                 .set_end(duration_clip)
                                 # Here you can add key sounds using `set_audio`.
                                 )
            text_index += 1
    empty = TextClip(
        'e',
        color='transparent',
        font='simhei',
        fontsize=fontsize,
        kerning=3,
    )
    clips_letters.append(empty
                         .set_position((-10, -10))
                         .set_start(tmp_duration)
                         .set_end(duration_effect)
                         # Here you can add key sounds using `set_audio`.
                         )
    return CompositeVideoClip(clips_letters, size=screensize)


text_list = [
    ['上苍不会让所有幸福集中到', '某个人身上'],
    ['得到了爱情未必拥有金钱', '拥有金钱未必得到快乐'],
]


def author_clip(author, width, dur):
    fontsize = 90
    tmp = '-- ' + author
    clip_text = TextClip(
        tmp,
        color='black',
        font='方正粗黑宋简体',
        # font='simhei',
        fontsize=fontsize,
        kerning=3,
    )
    x = width - len(tmp) * fontsize
    y = 950
    return clip_text.set_position((x, y)).set_end(dur)


def logo_clip(width, dur):
    fontsize = 70
    logo = '关注我，一起感悟人生'
    clip_text = TextClip(
        logo,
        color='white',
        font='方正粗黑宋简体',
        # font='simhei',
        fontsize=fontsize,
        kerning=3,
    )
    x = (width - len(logo) * fontsize) / 2
    y = 2100
    return clip_text.set_position((x, y)).set_end(dur)


def text_clip(text_list, width, height, duration, anim_dura):
    screensize = (width, height)
    clip_list = []
    start = 0
    for t in text_list:
        clip = clip_typewriter(t, duration, anim_dura, screensize).set_start(start).set_position('center')
        start += 3
        clip_list.append(clip)
    # clip_1 = clip_typewriter('测试中文能不能用', 2, 1).set_start(1).set_position('center')
    # clip_2 = clip_typewriter('world', 2, 1).set_start(4).set_position('center')
    # clip_final = CompositeVideoClip([clip_1, clip_2], size=screensize)
    clip_final = CompositeVideoClip(clip_list, size=screensize)
    return clip_final


if __name__ == '__main__':
    screensize = (1000, 1000)
    fps = 12
    clip_list = []
    start = 0
    for index, t in enumerate(text_list):
        print(str(start))
        clip = clip_typewriter(t, 3, 2, screensize).set_start(start).set_position('center')
        start += 3
        clip_list.append(clip)
    # clip_1 = clip_typewriter('测试中文能不能用', 2, 1).set_start(1).set_position('center')
    # clip_2 = clip_typewriter('world', 2, 1).set_start(4).set_position('center')
    # clip_final = CompositeVideoClip([clip_1, clip_2], size=screensize)
    clip_final = CompositeVideoClip(clip_list, size=screensize)
    clip_final.write_gif('test_typewriter.gif', fps=fps)
