import pandas as pd
import numpy as np
import sklearn.cross_validation
#from sklearn.neighbors import NearestNeighbors

def eucl(x1, x2):
    return np.sqrt(np.sum((x1-x2)*(x1-x2), axis=1))

def findkneighbors(X_train, Y_train, test, k=5):
    neighbors = list(range(0,k))
    for i in range(0,k):
        dist.append(eucl(X_train[i], test))
    for i in range(k, X_train.shape[0]):
        dis = eucl(X_train[i], test)
        if dis>

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

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.3, random_state=0)

for i in range(0, X_test.shape[0]):
    predictions = findkneighbors(X_train, Y_train, X_test[0])
