# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 02:06:44 2018

@author: Student

Find the suitable value of k for the given dataset CAR EVALUATION DATASET.
Use the obtained k value for developing KNN classifier
 
Report the classification accuracy

"""

import pandas as pd
import numpy as np
import sklearn.cross_validation as sk
import sklearn.linear_model as lm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

data = pd.read_csv('car.csv',names=['buying','maint','doors','persons','lug_boot','safety','class'])
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['maint'],_ = pd.factorize(data['maint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])
X = data.iloc[:,:-1]
y = data.iloc[:,-1]

rs = KFold(n_splits=24)
rs.get_n_splits(X)
KFold(n_splits=24, random_state=None, shuffle=False)

errors = []
for train_index, test_index in rs.split(X):
    X_test = X.iloc[test_index]
    X_train = X.iloc[train_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    test_errors = []
    
    for k in range(1,30):
        clf = KNeighborsClassifier(n_neighbors = k)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        test_errors.append(1-metrics.accuracy_score(y_test,y_pred))
    if len(errors):  
        errors = np.vstack([errors, test_errors])
    else:
        errors = np.hstack((errors, test_errors))
err = []
for i in range(0,29):
    err = np.append(err, np.mean(errors[:,i]))
print(err)
k = np.argmin(err)+1
print(k)
clf = KNeighborsClassifier(n_neighbors = k)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))
k_range = np.arange(1,30)
plt.plot(k_range, err, 'g--')
