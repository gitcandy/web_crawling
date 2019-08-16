import pandas as pd
import numpy as np
import csv


# *********************数据说明***********************
# 训练数据：src/step1/input/train.csv
# 测试数据：src/step1/input/test.csv
# 结果文件：src/output/test_prediction.csv
# ***************************************************
class LogisticRegression:
    def __init__(self):
        # 初始化模型
        self.coef_ = None
        self.intercept_ = None
        self.theta_ = None

    def sigmoid(self, x):
        return 1. / (1. + np.exp(-x))

        # 利用梯度法进行线性回归预测

    def fit(self, x_train, y_train, eta=0.01, n_iters=1e4):

        assert x_train.shape[0] == y_train.shape[0], "the size of x_train must be equal to y_train"

        def J(theta, x_b, y):

            y_hat = self.sigmoid(X_b.dot(theta))
            try:
                return - np.sum([y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)]) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            return X_b.T.dot(self.sigmoid(X_b.dot(theta)) - y) / len(y)

        def gradient_decent(x_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
            theta = initial_theta
            n_iter = 0
            while (n_iter < n_iters):
                gradient = dJ(theta, x_b, y)
                last_theta = theta
                theta = theta - eta * gradient

                if (np.abs(J(theta, x_b, y) - J(last_theta, x_b, y)) < epsilon):
                    break
                n_iter += 1
            return theta

        X_b = np.hstack([np.ones([len(x_train), 1]), x_train])
        initial_theta = np.zeros(X_b.shape[1])
        self.theta_ = gradient_decent(X_b, y_train, initial_theta, eta)
        self.coef_ = self.theta_[1:]
        self.intercept_ = self.theta_[0]
        return self

    def predict_proba(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果概率向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return self.sigmoid(X_b.dot(self.theta_))

    def predict(self, X_predict):
        """给定待预测数据集X_predict，返回表示X_predict的结果向量"""
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        proba = self.predict_proba(X_predict)
        return np.array(proba >= 0.5, dtype='int')

    def score(self, X_test, y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""

        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)

    def __prepare__(metacls, name, bases):
        return "LogisticRegression"


class PCA:
    def __init__(self, n_components):
        """初始化PCA"""
        assert n_components >= 1, "n_components must be valid"
        # 一共提取几个成分
        self.n_conmponents_ = n_components
        # 提取的成分为什么
        self.componets = None

    def fit(self, x, eta=0.01, n_iters=1e4):
        """获得数据集x的前n个主成分"""
        assert self.n_conmponents_ <= x.shape[1], "n_components must not be greater than the dimension of x"

        def demean(x):
            return x - np.mean(x, axis=0)

        def f(w, x):
            return np.sum((x.dot(w) ** 2)) / len(x)

        # 梯度函数
        def df(w, x):
            return x.T.dot(x.dot(w)) * 2. / len(x)

        def direction(w):
            return w / np.linalg.norm(w)

        def first_component(x, initial_w, eta, n_iters=1e4, epsilon=1e-8):
            w = direction(initial_w)

            n_iter = 0
            while (n_iter < n_iters):
                gradient = df(w, x)
                last_w = w
                w = w + eta * w
                w = direction(w)  # 求单位方向

                if (np.abs(f(w, x) - f(last_w, x)) < epsilon):
                    break
            n_iter += 1
            return w

        x_pca = demean(x)
        self.componets = np.empty(shape=(self.n_conmponents_, x.shape[1]))
        for i in range(self.n_conmponents_):
            initial_w = np.random.random(x_pca.shape[1])
            w = first_component(x_pca, initial_w, eta, n_iters)
            self.componets[i, :] = w
            # 求下一个主成分
            x_pca = x_pca - x_pca.dot(w).reshape(-1, 1) * w
        return self

    def tranform(self, x):
        """将给定的x映射到各个主成分的分量中"""
        assert self.componets.shape[1] == x.shape[1], "dimension must be equal"
        return x.dot(self.componets.T)

    def inverse_transform(self, x):
        """将给定的X反向映射会原来的空间"""
        assert x.shape[1] == self.componets.shape[1], "rols of x must be equal to cols of components"

        return x.dot(self.componets)

    def __repr__(self):
        return "PCA(n_components=%d)" % self.n_conmponents_


def getPrediction():
    ########## Begin ##########
    train_customer = pd.read_csv('E:/input/train.csv', header=0)
    test_customer = pd.read_csv('E:/input/test.csv', header=0)

    train = np.array(train_customer)
    test = np.array(test_customer)
    x_train = train[:, 1:52]
    y_train = train[:, 53]
    x_test = test[:, 1:52]
    pca = PCA(n_components=2)
    pca.fit(x_train)
    x_train_inverse = pca.tranform(x_train)
    lrg = LogisticRegression()
    lrg.fit(x_train_inverse, y_train)
    x_test_invers = pca.tranform(x_test)
    y_predict = lrg.predict(x_test_invers)
    data_test = pd.DataFrame({'ID': test[:, 0], 'TARGET': y_predict})
    data_test.to_csv('E:/output/test_prediction.csv')
    print("cheng goong")


    ########## End ##########
getPrediction()