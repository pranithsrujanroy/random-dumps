# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:47:15 2018

@author: Student
"""
import math

def pre_process_data(string_data):
    convertor = {
        'vhigh': 1,'high': 2,
        'med' : 3,
        'low' : 4,
        '5more' : 6,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        'more' : 5,
        'small' : 2,
        'big' : 4,
        'unacc' : 1,
        'acc' : 2,
        'good' : 3,
        'vgood' : 4
        }
    clean_data = []
    for record in string_data:
        clean_record = []
        for attribute in record:
            clean_record.append(convertor[attribute])
        clean_data.append(clean_record)
    return clean_data


def euclidean_dist(X, Y):
    if(len(X) != len(Y)):
        print("Vectors of different dimensions. Cannot compute distances")
        return -1
    square_sum = 0
    for i,j in zip(X,Y):
        square_sum = square_sum + (i-j)**2
    return math.sqrt(square_sum)

def record_distance(x1,x2):
    return euclidean_dist(x1,x2)

def k_nearest_neighbours(record,k,training_data,training_data_labels):
    distance_list = []
    for comp_record,label in zip(training_data,training_data_labels):
        distance_list.append([comp_record,record_distance(record,comp_record),label])
    #print(distance_list)
    distance_list.sort(key=lambda x : x[1],reverse=True)
    k_neighbours = []
    k_neighbours_label = []
    for i in range(k):
        d = distance_list[i]
        k_neighbours.append(d[0])
        k_neighbours_label.append(d[2])
    return k_neighbours,k_neighbours_label

def predict(record,nearest_neighbours,labels):
    #print(nearest_neighbours)
    #nearest_neighbours = testing_data[1:40]
    #labels = testing_data_labels[1:40]
    k_distance_list = []
    for neighbour in nearest_neighbours:
        k_distance_list.append(record_distance(record,neighbour))
    k_dist_max = max(k_distance_list)
    k_dist_min = min(k_distance_list)
    values = [0,0,0,0,0]
    for neighbour,label in zip(nearest_neighbours,labels):
        values[label] = values[label] + 1
        if(k_dist_max == k_dist_min):
            values[label] = values[label] + 1
        else:
            values[label] = values[label] + (k_dist_max - record_distance(record,neighbour) ) / (k_dist_max - k_dist_min)
    #print(values)
    pred_label = values.index(max(values))
    #print(pred_label)
    return pred_label
