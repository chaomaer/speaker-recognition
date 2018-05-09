import librosa
from librosa.feature import mfcc
import numpy as np
import sounddevice as sd
import glob
from scipy.io import wavfile
#    Store the sampling rate as `sr`

sd.default.samplerate = 16000   # 采样频率

# 播放
def play(filename):
    a = open(filename, 'rb').read()
    b = np.frombuffer(a, dtype=np.int16)
    # wavfile.write('hello.wav', sd.default.samplerate,b)
    sd.play(b)   # 播放包含音频数据的NumPy数组。
    sd.wait()


# files = glob.glob('train_data/*/an251-fash-b.raw', recursive=True)
# for f in files:
#     play(f)

play("temp.wav")
