import wave
import random
import numpy as np
from scipy.io import wavfile
from librosa import feature
import librosa
import time
from tqdm import tqdm,trange
import time
import pygame
import sounddevice as sd
import soundfile as sf
import tts
import stt
from gmm import ser


sd.default.samplerate = 16000  # 取样频率  16000
sd.default.channels = 1        # 单声道


def record(duration=3):        # 3s

    # print("开始录制")
    # blockig,布尔类型, 如果“False”（默认），立即返回（但录音
    # 在后台继续），如果“真”，则等待直到记录完成。
    # 非阻塞调用可以用stop（）或停止来停止
    # 通过`wait（）`进入一个阻塞状态。
    myrecording = sd.rec(duration*sd.default.samplerate, blocking=False)
    # 加入进度条
    for _ in tqdm(range(300), leave=False, bar_format='{l_bar}{bar}'):
        time.sleep(0.01)  # 进度条每0.1s前进一次，总时间为1000*0.1=100s
    # print("录制结束")
    sf.write('temp.wav', myrecording, sd.default.samplerate, subtype='PCM_16')
    text = stt.stt("temp.wav")  # speech to text
    return text


if __name__ == '__main__':
    target = "习大大"    # 说话人授权
    while True:
        text = record()  # 获取语音输入
        print(text)
        if text is None:
            time.sleep(2)
            continue
        if text.find("希望") != -1:  # 授权，唤醒词
            label = ser.record_predict("temp.wav", "../gmm/model.out")
            if label == target:
                break
            tts.tts(label+"你没有语音控制权限")
            continue
    tts.tts(label+"你好，"+"你已经通过权限认证")
    while True:
        tts.tts("请输入语音指令")
        text = record()
        print("语音指令:"+text)
        print("说话人: ", end='')
        label = ser.record_predict("temp.wav", "../gmm/model.out")
        print(label)
        time.sleep(2)

