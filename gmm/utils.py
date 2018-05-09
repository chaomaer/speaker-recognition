from scipy.io import wavfile

def read_wav(fname):
    # 打开一个WAV文件
    # 返回采样率（以采样/秒）和WAV文件中的数据。
    fs, signal = wavfile.read(fname)
    assert len(signal.shape) == 1, "Only Support Mono Wav File!"
    return fs, signal
