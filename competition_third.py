import pandas as pd
import numpy as np
import csv


# *********************数据说明***********************
# 训练数据：src/step1/input/train.csv
# 测试数据：src/step1/input/test.csv
# 结果文件：src/output/test_prediction.csv
# ***************************************************
class LinearRegression:
    def __init__(self):
        """初始化linear regression模型"""
        # 初始化方程系数
        self.coef_ = None
        # 初始化截距
        self.interception_ = None
        # 初始化整体的系数向量theta
        self.theta_ = None

    def fit_normal(self, x_train, y_train):
        """用于训练数据集"""
        assert x_train.shape[0] == y_train.shape[0], "the size of x_train must be equal to y_train"
        # x的向量，第一列x0默认为全为1
        x_b = np.hstack([np.ones((len(x_train), 1)), x_train])
        # 求方程的theta值，用多元线性回归的正规方程解的方式
        self.theta_ = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y_train)
        self.interception_ = self.theta_[0]
        self.coef_ = self.theta_[1:]
        return self

    def predict(self, x_predict):
        assert self.coef_ is not None and self.interception_ is not None, "must fit before predict"
        assert x_predict.shape[1] == len(self.coef_), "the feature number of x_predict must be equal to x_train"
        x_b = np.hstack([np.ones((len(x_predict), 1)), x_predict])
        return x_b.dot(self.theta_)

    def J(theta, x_b, y):
        """进行计算目标函数"""
        try:
            return np.sum((y - x_b.dot(theta)) ** 2) / len(x_b)
        except:
            return float('inf')

    # 利用梯度法进行线性回归预测
    def fit_gd(self, x_train, y_train, eta=0.01, n_iters=1e4):
        assert x_train.shape[0] == y_train.shape[0], "the size of x_train must be equal to y_train"

        def J(theta, x_b, y):
            try:
                return np.sum((y - x_b.dot(theta)) ** 2) / len(x_b)
            except:
                return float('inf')

        def dJ(theta, x_b, y):
            """用于求偏导"""
            res = np.empty(len(theta))
            res[0] = np.sum(x_b.dot(theta) - y)
            for i in range(1, len(theta)):
                res[i] = (x_b.dot(theta) - y).dot(x_b[:, i])
            return res * 2 / len(x_b)

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

        x_b = np.hstack([np.ones([len(x_train), 1]), x_train])
        initial_theta = np.zeros(x_b.shape[1])
        self.theta_ = gradient_decent(x_b, y_train, initial_theta, eta)
        self.coef_ = self.theta_[1:]
        self.interception_ = self.theta_[0]
        return self

    def fit_sgd(self, x_train, y_train, n_iters=5, t0=5, t1=50):
        """n_iters在这里可以理解成我们要对我们的样本看几圈"""
        assert x_train.shape[0] == y_train.shape[0], "the size of x_train must be equal to y_train"
        assert n_iters >= 1, "n_iters must be at least 1"

        def dJ_sgd(theta, X_b_i, y_i):
            return 2 * X_b_i.T.dot(X_b_i.dot(theta) - y_i)

        def sgd(X_b, y, initial_theta, n_iters, t0=5, t1=50):

            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            m = len(X_b)
            for cur_iter in range(n_iters):

                indexs = np.random.permutation(m)
                X_b_new = X_b[indexs]
                y_new = y[indexs]
                for i in range(m):
                    gradient = dJ_sgd(theta, X_b_new[i], y_new[i])
                    theta = theta - learning_rate(cur_iter * m + i) * gradient

            return theta

        X_b = np.hstack([np.ones((len(x_train), 1)), x_train])
        initial_theta = np.zeros(X_b.shape[1])
        self.theta_ = sgd(X_b, y_train, initial_theta, n_iters, t0, t1)
        self.coef_ = self.theta_[1:]
        self.interception_ = self.theta_[0]
        return self


def getPrediction():
    ########## Begin ##########
    train_customer = pd.read_csv('src/step1/input/train.csv', header=0)
    test_customer = pd.read_csv('src/step1/input/test.csv', header=0)

    train = np.array(train_customer)
    test = np.array(test_customer)
    x_train = train[:, 1:52]
    y_train = train[:, 53]

    x_test = test[:, 1:52]

    lrg = LinearRegression()
    lrg.fit_gd(x_train, y_train)
    y_predict = lrg.predict(x_test)
    predict_data = pd.DataFrame([test[:, 0], y_predict], columns=['ID', 'TARGET'])
    predict_data.to_csv('src\output\test_prediction.csv', indexs=0)











    ########## End ##########
