# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:46:38 2018

@author: Pranith Srujan Roy
"""
"""
Find a suitable value of k for CAR EVALUATION DATASET. Use the obtained k-value for developing 
KNN classifier.
"""
import pandas as pd
import sklearn as sk


dat = pd.read_csv('data.txt',names=['buying','maint','doors','persons','lug_boot','safety','class'])
dat['class'],class_names = pd.factorize(dat['class'])
dat['buying'],_ = pd.factorize(dat['buying'])
dat['maint'],_ = pd.factorize(dat['maint'])
dat['doors'],_ = pd.factorize(dat['doors'])
dat['persons'],_ = pd.factorize(dat['persons'])
dat['lug_boot'],_ = pd.factorize(dat['lug_boot'])
dat['safety'],_ = pd.factorize(dat['safety'])
X = dat.iloc[:,:-1]
y = dat.iloc[:,-1]

#print X
#print y
X_train, X_test, y_train, y_test = sk.cross_validation.train_test_split(X, y, test_size=0)

findk(X_train, y_train)
#test = pd.DataFrame([[0,0,0,0,0,0]])
#print X_train.shape[0]
#print(neigh.predict(X_test))

#print(neigh.kneighbors(X_test))


