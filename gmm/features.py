from python_speech_features import mfcc
import numpy as np
import sys

# 提取语音特征
# 使用mfcc
def get_feature(fs, signal):
    mfcc_feature = mfcc(signal, fs)  # mfcc() 返回：包含特征的大小为NUMFRAMES的数组（NUMFRAMES）。每行保存1个特征向量。
    assert(len(mfcc_feature)>0)  # 若为真，继续执行
    return mfcc_feature
