# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 04:14:05 2018

@author: Student
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import cross_val_score
from collections import Counter
import sklearn

def findk(X_train,y_train):
    myList = list(range(1,50))
    neighbors = filter(lambda x: x % 2 != 0, myList)
    cv_scores = []
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn,X_train,y_train,cv=10, scoring='accuracy')
        cv_scores.append(scores.mean())
        MSE = [1 - x for x in cv_scores]
        optimal_k = neighbors[MSE.indemin(MSE)]
    return optimal_k,MSE
     
data = pd.read_csv('data.txt',names=['buying','maint','doors','persons','lug_boot','safety','class'])
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['maint'],_ = pd.factorize(data['maint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)
k,MSE = findk(X_train,y_train)
print(k)
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(accuracy_score(y_test, pred))
myList = list(range(1,50))
neighbors = filter(lambda x: x % 2 != 0, myList)
plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()
