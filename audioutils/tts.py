from aip import AipSpeech
import playsound
import uuid
import os
import io
import time
import shutil
import random
import string

""" 你的 APPID AK SK """
APP_ID = '10930939'
API_KEY = 'XuG0Vi7dD825PMmuXW3dQDmD'
SECRET_KEY = 'OGA8kuWcu5NZiWofvq8riwvvhMaDDyjk'

def genname():
    s = ''
    for _ in range(15):
        s += random.choice(string.ascii_letters + string.digits)
    return s+'.mp3'


def tts(content='我爱你,中国,我的母亲'):
    temp = "log/"+genname()
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(content, 'zh', 1, {
        'vol': 10,
        'per': 0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    with open(temp, 'wb') as f:
        f.write(result)
        f.flush()
        f.close()
        playsound.playsound(temp)
        os.remove(temp)


if __name__ == '__main__':
    tts()
