# -*- coding: UTF-8 -*-
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import datetime
from random import sample

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


def clip(sub_video_list, duration):
    main_video = r"D:\视频\书单\main.mp4"
    clip1 = VideoFileClip(main_video)
    video_list = [clip1]
    start = 0
    for v in sub_video_list:
        print(v)
        clip2 = VideoFileClip(v)
        width, height = clip1.size
        clip_duration = min(duration, clip2.duration)
        clip2 = clip2.resize(width=width, height=width*3/5).set_position((0, 600)).set_start(start).set_duration(clip_duration).fx(
            vfx.colorx, 1.6)
        video_list.append(clip2)
        start += clip_duration
    CompositeVideoClip(video_list).write_videofile(r'pip.mp4')


def clip2(sub_video_list, duration, index):
    clip1 = VideoFileClip(sub_video_list[0])
    video_list = []
    start = 0
    for v in sub_video_list:
        print(v)
        clip2 = VideoFileClip(v)
        width, height = clip1.size
        clip_duration = min(duration, clip2.duration)
        clip2 = clip2.resize(width=width).set_start(start).set_duration(clip_duration).fx(vfx.colorx, 1.8)
        video_list.append(clip2)
        start += clip_duration
    CompositeVideoClip(video_list).write_videofile('pip' + str(index) + '.mp4')


def main(index=0):
    start_time = datetime.datetime.now()
    snippet_duration = 5
    all_duration = 35
    sub_video_list = filter_video()
    num = int(all_duration / snippet_duration)
    sub_video_list = random_sub_video(sub_video_list, num)
    # clip(sub_video_list, snippet_duration)
    clip2(sub_video_list, snippet_duration, index)
    end_time = datetime.datetime.now()
    print("cost: " + str((end_time - start_time).seconds))


def main_bg():
    start_time = datetime.datetime.now()
    snippet_duration = 5
    all_duration = 70
    sub_video_list = filter_video()
    num = int(all_duration / snippet_duration)
    sub_video_list = random_sub_video(sub_video_list, num)
    clip(sub_video_list, snippet_duration)
    # clip2(sub_video_list, snippet_duration)
    end_time = datetime.datetime.now()
    print("cost: " + str((end_time - start_time).seconds))


if __name__ == '__main__':
    # filter_video()
    # filter_portrait_video()
    for i in range(0, 9):
        # _thread.start_new_thread(main, (i,))
        main(i)
    # main_bg()