
from sklearn import datasets
from sklearn.model_selection import train_test_split
#import regression classes
from Regression import Regression as Reg
from Regression import LinearRegression
from Regression import RidgeRegression


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],
                                                    dataset['target'],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
models = [LinearRegression(), RidgeRegression(alpha)]

for model in models:
    model.fit(X_train, y_train)
    params = model.get_params()
    beta = params['coef']
    intercept = params['intercept']
    R2 = model.score(X_train,y_train)
    print(f'The best coefficients of the {model.__class__.__name__} are {beta} and the intercept is {intercept} /n the R^2 is {R2}')
