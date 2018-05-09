import os
import itertools
import glob
import argparse
from utils import read_wav
from interface import ModelInterface
import sys


def get_args():
    # 说话人识别命令行工具
    desc = "Speaker Recognition Command Line Tool"
    '''
        每个输入目录中的Wav文件将被标记为目录的基本名称。
    请注意，通配符输入应该*引号*，并且它们将被发送到glob.glob模块。
    例子：
      培训（在相应目录下注册一个名为person *和mary的人员名单，并带有wav文件）：
      ./ser.py -t enroll -i“/ tmp / person * ./mary”-m model.out
      预测（预测所有wav文件的发言人）：
       ./ser.py -t预测-i“./*.wav”-m model.out
    '''
    epilog = """
Wav files in each input directory will be labeled as the basename of the directory.
Note that wildcard inputs should be *quoted*, and they will be sent to glob.glob module.
Examples:
    Train (enroll a list of person named person*, and mary, with wav files under corresponding directories):
    ./ser.py -t enroll -i "/tmp/person* ./mary" -m model.out
    Predict (predict the speaker of all wav files):
    ./ser.py -t predict -i "./*.wav" -m model.out
"""
    parser = argparse.ArgumentParser(description=desc, epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-t', '--task',
                        help='Task to do. Either "enroll" or "predict"',
                        required=True)

    parser.add_argument('-i', '--input',
                        help='Input Files(to predict) or Directories(to enroll)',
                        required=True)

    parser.add_argument('-m', '--model',
                        help='Model file to save(in enroll) or use(in predict)',
                        required=True)

    ret = parser.parse_args()
    return ret


def task_enroll(input_dirs, output_model):
    m = ModelInterface()
    input_dirs = [os.path.expanduser(k) for k in input_dirs.strip().split()]
    dirs = itertools.chain(*(glob.glob(d) for d in input_dirs))
    dirs = [d for d in dirs if os.path.isdir(d)]

    if len(dirs) == 0:
        print("No valid directory found!")
        sys.exit(1)

    for d in dirs:
        label = os.path.basename(d.rstrip('/'))
        wavs = glob.glob(d + '/*.wav')

        if len(wavs) == 0:
            print("No wav file found in %s" % (d))
            continue
        for wav in wavs:
            try:
                fs, signal = read_wav(wav)
                m.enroll(label, fs, signal)
                print("wav %s has been enrolled" % (wav))
            except Exception as e:
                print(wav + " error %s" % (e))

        m.train()
        m.dump(output_model)


def task_predict(input_files, input_model):
    total = 0
    acc = 0
    m = ModelInterface.load(input_model)
    for f in glob.glob(os.path.expanduser(input_files)):
        total += 1
        fs, signal = read_wav(f)
        label = m.predict(fs, signal)
        print(f, '->', label, end=''),
        if f.split('/')[-2] == label:
            print("√")
            acc += 1
        else:
            print('×')

    acc = acc*1.0/total
    print(acc)


def record_predict(input_file, input_model):
    m = ModelInterface.load(input_model)
    fs, signal = read_wav(input_file)
    label = m.predict(fs, signal)
    return label


if __name__ == "__main__":
    global args
    args = get_args()

    task = args.task
    if task == 'enroll':
        task_enroll(args.input, args.model)
    elif task == 'predict':
        task_predict(args.input, args.model)
