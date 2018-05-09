import pickle
from collections import defaultdict
from skgmm import GMMSet
from features import get_feature
import time

class ModelInterface:

    def __init__(self):
        self.features = defaultdict(list)
        self.gmmset = GMMSet()

    def enroll(self, name, fs, signal):
        feat = get_feature(fs, signal)
        self.features[name].extend(feat)
    # 使用高斯混合模型，训练
    def train(self):
        self.gmmset = GMMSet()
        start_time = time.time()
        for name, feats in self.features.items():
            try:
                self.gmmset.fit_new(feats, name)
            except Exception as e :
                print ("%s failed"%(name))
        print (time.time() - start_time, " seconds")
    # 转储所有模型到文件“
    def dump(self, fname):
        """ dump all models to file"""
        self.gmmset.before_pickle()
        with open(fname, 'wb') as f:
            pickle.dump(self, f, -1)
        self.gmmset.after_pickle()
    # 返回一个标签（名称）
    def predict(self, fs, signal):
        """
        return a label (name)
        """
        try:
            feat = get_feature(fs, signal)
        except Exception as e:
            print (e)
        return self.gmmset.predict_one(feat)

    @staticmethod
    def load(fname):
        """ load from a dumped model file"""  # 从转储的模型文件加载
        with open(fname, 'rb') as f:
            R = pickle.load(f)
            R.gmmset.after_pickle()
            return R
