import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
import sqlite3


def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    cursor = db.cursor()
    model_params = model.get_params()
    for param_, value in model_params.items():
        model_params_to_insert = (int(model_id), model_desc, param_, value)
        cursor.execute('''INSERT INTO model_params 
                  (id, desc, param_name, value) VALUES (?, ?, ?, ?)''', model_params_to_insert)

    model_coef = model.coef_[0]

    for i, val in enumerate(model_coef):
        feature_name = X_train.columns[i]
        coef_to_insert = (int(model_id), model_desc, feature_name, val)
        cursor.execute('''INSERT INTO model_coefs 
                  (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''', coef_to_insert)
    intercept_to_insert = (int(model_id), model_desc, 'intercept', model.intercept_[0])
    cursor.execute('''INSERT INTO model_coefs 
          (id, desc, feature_name, value) VALUES (?, ?, ?, ?)''', intercept_to_insert)

    results_to_insert = (int(model_id), model_desc, train_score, test_score)
    cursor.execute('''INSERT INTO model_results 
          (id, desc, train_score, test_score) VALUES (?, ?, ?, ?)''', results_to_insert)

    db.commit()


# connect to sqlite
db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER, 
               desc TEXT, 
               param_name TEXT, 
               value FLOAT)''')
db.commit()

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER, 
               desc TEXT, 
               feature_name TEXT, 
               value FLOAT)''')
db.commit()

cursor.execute('''CREATE TABLE model_results (
               id INTEGER, 
               desc TEXT, 
               train_score FLOAT, 
               test_score FLOAT)''')
db.commit()


# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=87)

# Fit baseline model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, "Baseline model", db, baseline_model, X_train, X_test, y_train, y_test)

# Fit the reduced logistic regression model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, "Reduced model", db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# Logistic regression model with L1 penalty
penal_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penal_model.fit(X_train, y_train)
save_to_database(3, "L1 penalty model", db, penal_model, X_train, X_test, y_train, y_test)


cursor = db.cursor()
query = '''SELECT id, test_score FROM model_results WHERE test_score = (SELECT MAX(test_score) FROM model_results) '''
model_info = cursor.execute(query).fetchall()
best_model_id = model_info[0][0]
best_test_score = model_info[0][1]
print("Best model id is {} and the best test score is {}.".format(best_model_id,best_test_score))


# get coefs for all the params
query = '''SELECT feature_name, value FROM model_coefs WHERE id == {}'''.format(best_model_id)
feature_info = cursor.execute(query).fetchall()

for row in feature_info:
    print("{}: {}".format(row[0], row[1]))

# retrain the model
test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
coef = [row[1] for row in feature_info][:-1]
intercept = feature_info[-1][1]
test_model.coef_ = np.array([coef])
test_model.intercept_ = np.array([intercept])

# reproduce
test_score = test_model.score(X_test, y_test)
print(f'The best reproduced test score is {test_score}')

db.close()
