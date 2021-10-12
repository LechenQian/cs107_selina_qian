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
        X = np.append(x, [[1]] * len(y), axis=1)
        M = self.alpha * np.eye(X.shape[1])
        Beta = np.dot(np.linalg.pinv(np.dot(X.T, X) + np.dot(M.T, M)), np.dot(X.T, y))

        self.params['coef'] = Beta[:-1]
        self.params['intercept'] = Beta[-1]
        # return self.params['coef'], self.params['intercept']
