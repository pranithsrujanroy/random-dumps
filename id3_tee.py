# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 01:56:33 2018

@author: Student
"""
import sklearn as sk
import pandas as pd
from id3 import Id3Estimator
from id3 import export_graphviz


data = pd.read_csv('car.data.txt',names=['buying','maint','doors','persons','lug_boot','safety','class'])
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['maint'],_ = pd.factorize(data['maint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = sk.cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)
estimator = Id3Estimator()
estimator.fit(X_train, y_train)
export_graphviz(estimator.tree_, 'tree.dot', data['class'])


import graphviz
#dot -T p