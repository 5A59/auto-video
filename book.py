# -*- coding: UTF-8 -*-
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import datetime
from random import sample

import text
import music
import content

from moviepy.editor import *
import _thread


def filter_start_video():
    dir_list = [
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\Meteor',
    ]
    video_list = []
    for d in dir_list:
        for fpath, dirs, fs in os.walk(d):
            for f in fs:
                if f.endswith('.mp4'):
                    video = os.path.join(fpath, f)
                    clip1 = VideoFileClip(video)
                    if clip1.w <= clip1.h:
                        clip1.close()
                        print('delete: ' + video)
                        os.remove(video)
                        # video_list.append(video)
    return video_list


def filter_portrait_video():
    dir_list = [
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\我在天空贩卖温柔',
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\地山小吉'
    ]
    video_list = []
    for d in dir_list:
        for fpath, dirs, fs in os.walk(d):
            for f in fs:
                if f.endswith('.mp4'):
                    video = os.path.join(fpath, f)
                    clip1 = VideoFileClip(video)
                    if clip1.w <= clip1.h:
                        clip1.close()
                        print('delete: ' + video)
                        os.remove(video)
                        # video_list.append(video)
    return video_list


def filter_video():
    dir_list = [
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品',

        # 壮阔
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\扛相机的陈同学',
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\长城摄影师杨东'

        # 通用
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\Meteor',
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\Frank',

        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\Deepsea',
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\Oblivion'

        r'D:\Software\抖音采集工具x64\作品保存\作者作品\Forevil',
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\Transparent',
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\大理阿飞',
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\我在天空贩卖温柔',
        r'D:\Software\抖音采集工具x64\作品保存\作者作品\地山小吉',
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\初弦'

        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\yanhua',

        # 古风
        # r'D:\Software\抖音采集工具x64\作品保存\gufeng' # gufeng
        # no use
        # r'D:\Software\抖音采集工具x64\作品保存\作者作品\KKDai',
    ]
    video_list = []
    # video_dir = r'D:\Software\抖音采集工具x64\作品保存\作者作品\Frank'
    # video_dir = r'D:\Software\抖音采集工具x64\作品保存\gufeng'
    for d in dir_list:
        for fpath, dirs, fs in os.walk(d):
            for f in fs:
                if f.endswith('.mp4'):
                    video = os.path.join(fpath, f)
                    video_list.append(video)
    return video_list


def random_sub_video(video_list, num):
    return sample(video_list, num)


def bg_clip():
    main_video = r"D:\视频\书单\bg.mp4"
    clip1 = VideoFileClip(main_video)
    return clip1


def clip(video_list, bg_clip, sub_video_list, duration, all_dur):
    start = 0
    last_dur = all_dur
    for index, v in enumerate(sub_video_list):
        print(v)
        clip2 = VideoFileClip(v).without_audio()
        width, height = bg_clip.size
        clip_duration = min([duration, clip2.duration, last_dur])
        last_dur -= clip_duration
        clip2 = clip2.resize(width=width).set_start(start).set_position((0, 1200)).set_duration(clip_duration).fx(vfx.colorx, 1.8)
        print('height: ' + str(clip2.size))
        video_list.append(clip2)
        start += clip_duration


# return text_clip, duration
def clip_text(text_list, clip_bg):
    width, height = clip_bg.size
    return text.text_clip(text_list, width, height, 3, 2), len(text_list) * 3


def main_bg(author, text_list, index):
    clip_bg = bg_clip()
    print(str(clip_bg.size))

    # 文案
    clip_t, duration = clip_text(text_list, clip_bg)
    w, h = clip_bg.size
    clip_a = text.author_clip(author, w, duration)
    clip_logo = text.logo_clip(w, duration)

    # 视频
    video_list = []
    length = int(duration / clip_bg.duration) + 1
    for i in range(length):
        tmp = bg_clip()
        if i == length - 1:
            video_list.append(tmp.set_start(i * clip_bg.duration).set_duration(duration % clip_bg.duration))
        else:
            video_list.append(tmp.set_start(i * clip_bg.duration))

    start_time = datetime.datetime.now()
    snippet_duration = 5
    all_duration = duration
    print("duration: " + str(all_duration))
    sub_video_list = filter_video()

    num = int(all_duration / snippet_duration) + 1
    sub_video_list = random_sub_video(sub_video_list, num)

    clip(video_list, clip_bg, sub_video_list, snippet_duration, all_duration)

    video_list.append(clip_t)
    video_list.append(clip_a)
    video_list.append(clip_logo)

    CompositeVideoClip(video_list).set_audio(music.music_clip(duration)).write_videofile(r'./out/pip' + str(index) + '.mp4')
    end_time = datetime.datetime.now()
    print("cost: " + str((end_time - start_time).seconds))


def main():
    content_list = content.read_content()
    for index, c in enumerate(content_list):
        # if index <= 4:
        #     continue
        main_bg(c.author, c.text_list, index)


if __name__ == '__main__':
    main()
