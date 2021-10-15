from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# import regression classes
from Regression import Regression as Reg
from Regression import LinearRegression
from Regression import RidgeRegression

dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)
alpha = None
LinearR2s = []
RidgeR2s = []
models = [LinearRegression(), RidgeRegression(alpha)]
alphas = [0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.56, 5.12, 10]
for alpha in alphas:
    for model in models:
        model.set_params(alpha=alpha)
        model.fit(X_train, y_train)
        params = model.get_params()
        beta = params['coef']
        intercept = params['intercept']
        R2 = model.score(X_test, y_test)
        if model.__class__.__name__ == 'LinearRegression':
            LinearR2s.append(R2)
        else:
            RidgeR2s.append(R2)
## figure
plt.figure(figsize=(8, 5))
plt.plot(alphas, LinearR2s, label='Linear Regression', color='r')
plt.plot(alphas, RidgeR2s, label='Ridge Regression', color='b')
plt.xlabel('alphas')
plt.ylabel("R^2")
plt.title('R^2  versus α in two types of regressions')
plt.legend()
plt.savefig('P2F.png')
plt.show()
