# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 01:44:10 2018

@author: Student
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import tree, metrics

dat = pd.read_csv('car.data.txt',names=['buying','maint','doors','persons','lug_boot','safety','class'])
dat['class'],class_names = pd.factorize(dat['class'])
dat['buying'],_ = pd.factorize(dat['buying'])
dat['maint'],_ = pd.factorize(dat['maint'])
dat['doors'],_ = pd.factorize(dat['doors'])
dat['persons'],_ = pd.factorize(dat['persons'])
dat['lug_boot'],_ = pd.factorize(dat['lug_boot'])
dat['safety'],_ = pd.factorize(dat['safety'])
X = dat.iloc[:,:-1]
y = dat.iloc[:,-1]
X_train, X_test, y_train, y_test = sk.cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)

dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
dtr = dtree.fit(X_train, y_train)

# use the model to make predictions with the test data
y_pred = dtree.predict(X_test)
# how did our model perform?
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))

import graphviz
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\bin'
dot_data = tree.export_graphviz(dtr, out_file='tree.pdf')
graph = graphviz.Source(dot_data)
graph.render('dat')

#dot_data = tree.export_graphviz(dtr, out_file='tree.dot', 
#                         feature_names=data['class'],  
#                         class_names=class_names,  
#                         filled=True, rounded=True,  
#                         special_characters=True)
#graph = graphviz.Source(dot_data)
#graph