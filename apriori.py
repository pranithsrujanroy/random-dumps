# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 01:44:51 2018

@author: 115cs0246
"""
def create_data_set():
    n = int(input("Enter the number of transactions"))
    dataset = []
    for i in range(0,n):
        l = raw_input().split()
        dataset.append(l)
    return dataset

def create_C1(dataset):
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
                
    c1.sort()
    return list(map(frozenset, c1))
    
def create_L(dataset, c1, min_sup):
    count_ck = {}
    for transaction in dataset:
        for ck in c1:
            if ck.issubset(transaction):
                if not ck in count_ck:
                    count_ck[ck] = 1
                else:
                    count_ck[ck] += 1
    len_dataset = float(len(dataset))
    L1 = []
    support_data = {}
    for key in count_ck:
        support = count_ck[key]/len_dataset
        if support >= min_sup:
            L1.insert(0,key)
        support_data[key] = support
    return L1, support_data

def aprioriGen(L, k):
    retlist = []
    lenL = len(L)
    for i in range(lenL):
        for j in range(i+1, lenL):
            L1 = list(L[i])[:k-2]
            L2 = list(L[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1==L2:
                retlist.append(L[i] | L[j])
    return retlist
    
def apriori(dataset, min_sup=0.5):
    C1 = create_C1(dataset)
    d = list(map(set, dataset))
    L1, support_data = create_L(d, C1, min_sup)
    L = [L1]
    k = 2
    while len(L[k-2])>0:
        ck = aprioriGen(L[k-2], k)
        Lk, supk = create_L(d, ck, min_sup)
        support_data.update(supk)
        L.append(Lk)
        k = k+1
    return L, support_data

dataset = create_data_set()
#L, support_data = apriori(dataset)

def calcConf(freqSet, H, supportData, brl, minConf=0.75):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf >= minConf: 
            print (freqSet-conseq,'-',conseq,'conf:',conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.75):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m+1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
    
def generateRules(L, supportData, minConf=0.75):  
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList
    
L,suppData= apriori(dataset,min_sup=0.5)
print(L)
rules= generateRules(L,suppData, minConf=0.75)