import numpy as np


class Regression:

    def __init__(self):
        self.params = {}
        self.alpha = 0.1

    def get_params(self):
        return self.params

    def set_params(self, **kwargs):
        for key, val in kwargs.items():
            if key in ('coef', 'intercept'):
                self.params[key] = val
            elif key == 'alpha':
                self.alpha = val
            else:
                raise TypeError("invalid argument '%s'" % key)

    def fit(self, x, y):
        raise NotImplementedError

    def predict(self, x):
        pred_y = np.dot(self.params['coef'], x) + np.dot(self.params['intercept'], np.ones(x.shape[0]))
        return pred_y

    def score(self, x, y):
        beta1 = self.params['coef']
        beta0 = self.params['intercept']
        pred_y = np.dot(x, beta1) + np.dot(np.ones(x.shape[0]), beta0)
        SST = np.sum((y - np.mean(y)) ** 2)
        SSE = np.sum((y - pred_y) ** 2)
        score = 1 - SSE / SST
        return score


class LinearRegression(Regression):
    def fit(self, x, y):
        X = np.append(x, [[1]] * len(y), axis=1)
        beta = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
        self.params['coef'] = beta[:-1]
        self.params['intercept'] = beta[-1]
        # return self.params['coef'], self.params['intercept']


class RidgeRegression(Regression):
    def __init__(self, alpha=0.1):
        super().__init__()
        self.alpha = alpha

    def fit(self, x, y):

        # center and scale data
        ymean = np.mean(y)
        Xmean = np.mean(x, axis=0)
        scale = 1 / np.sqrt(np.sum((x - Xmean) ** 2, axis=0))
        Xs = (x - Xmean) * scale
        ys = y - ymean

        gamma = self.alpha * np.identity(Xs.shape[1])
        beta = np.linalg.pinv(Xs.T.dot(Xs) + gamma.T.dot(gamma)).dot(
            Xs.T).dot(ys)
        beta *= scale
        self.params['coef'] = beta
        self.params['intercept'] = ymean - Xmean.dot(beta)
