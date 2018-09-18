# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 01:49:27 2018

@author: Pranith Srujan Roy
ref: http://thardes.de/big-data-englisch/frequent-pattern-fp-growth-algorithm/
"""

def create_dataset():
    n = int(input("Enter the number of transactions"))
    dataset = []
    for i in range(0,n):
        l = raw_input().split()
        dataset.append(l)
    return dataset

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
    
class treeNode:
    def __init__(self, name, occurance, parentNode):
        self.name = name
        self.count = occurance
        self.nodelink = None
        self.children = {}
        self.parent = parentNode
    
    def inc(self, increment):
        self.count += increment
        
    def display(self, idx=1):
        print('  '*idx, self.name, ' ', self.count)
        for child in self.children.values():
            child.display(idx+1)

def updateHeader(nodeToTest, targetNode):   
    while (nodeToTest.nodeLink != None):    
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode            

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count) 
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)    
    
def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in headerTable:
        if headerTable[k] < minSup: 
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]  
    retTree = treeNode('Null Set', 1, None) 
    for tranSet, count in dataSet.items():  
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable 
    
def ascendTree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
        
def findPrefixPath(basePat, treeNode): 
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats



    
dataset = create_dataset()



#fptree, header = createTree(dataset,3)
#fptree.disp()

import pyfpgrowth
dataset = create_dataset()
patterns = pyfpgrowth.find_frequent_patterns(dataset, 4)
rules = pyfpgrowth.generate_association_rules(patterns, 0.5)
print(rules)