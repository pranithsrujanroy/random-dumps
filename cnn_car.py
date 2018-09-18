# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 02:02:14 2018

@author: Student
"""

import pandas as pd
import numpy as np
import sklearn.cross_validation
#from sklearn.neighbors import NearestNeighbors

def eucl(x1, x2):
    return np.sqrt(np.sum(((x1-x2)*(x1-x2)),axis=1))

def findneighbor(sx,x):
    m = sx.shape[0]
    dist = 0
    for i in range(0, m):
        d = eucl(sx[i],np.array(x).reshape(1,-1))
        #print(d)
        if dist==0:
            dist = d
            idx = i
        else:
            if dist>d:
                dist = d
                idx = i
    return idx

data = pd.read_csv('car.data.txt', names=['buying','maint','doors','persons','lug_boot','safety','class'])
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['doors'],_ = pd.factorize(data['doors'])
data['maint'],_ = pd.factorize(data['maint'])
data['persons'],_=pd.factorize(data['persons'])
data['lug_boot'],_=pd.factorize(data['lug_boot'])
data['safety'],_=pd.factorize(data['safety'])
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]
X,_,Y,_ = sklearn.cross_validation.train_test_split(X,Y,test_size=0.0)
sx = np.array(X.iloc[0]).reshape(1,-1)
sy = np.array(Y.iloc[0]).reshape(1,-1)

#print(sy.shape)
for i in range(1,1728):
    x = X.iloc[i]
    idx = findneighbor(sx,x)
    if Y.iloc[i]==sy[idx]:
        pass
    else:
        sx = np.vstack((sx,x))
        sy = np.vstack((sy,Y.iloc[i]))
        
print(sx.shape)
print(sy.shape)