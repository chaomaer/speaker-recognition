from aip import AipSpeech
import playsound
import os
# 百度的aip


""" 你的 APPID AK SK """
APP_ID = '10930939'
API_KEY = 'XuG0Vi7dD825PMmuXW3dQDmD'
SECRET_KEY = 'OGA8kuWcu5NZiWofvq8riwvvhMaDDyjk'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件内容
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
def stt(filename, format='wav', sr=16000):
    data = client.asr(get_file_content(filename), format, sr)
    if data['err_no'] == 0:
        return data['result'][0]


if __name__ == '__main__':
    pass