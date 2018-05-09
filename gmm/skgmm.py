from sklearn.mixture import GMM
from sklearn.mixture import GaussianMixture
import operator
import numpy as np
'''
sklearn是基于numpy和scipy的一个机器学习算法库，它让我们能够使用同样的接口来实现所有不同的算法调用
'''
class GMMSet:

    def __init__(self, gmm_order = 32):
        self.gmms = []
        self.gmm_order = gmm_order
        self.y = []

    def fit_new(self, x, label):
        self.y.append(label)
        gmm = GaussianMixture(self.gmm_order)  # GMM
        gmm.fit(x)
        self.gmms.append(gmm)

    def gmm_score(self, gmm, x):
        return np.sum(gmm.score(x))
    # 预测
    # 通过概率分布判断确定说话人
    def predict_one(self, x):
        scores = [self.gmm_score(gmm, x) / len(x) for gmm in self.gmms]
        p = sorted(enumerate(scores), key=operator.itemgetter(1), reverse=True)
        p = [(str(self.y[i]), y, p[0][1] - y) for i, y in p]
        result = [(self.y[index], value) for (index, value) in enumerate(scores)]
        p = max(result, key=operator.itemgetter(1))
        return p[0]

    def before_pickle(self):
        pass

    def after_pickle(self):
        pass
