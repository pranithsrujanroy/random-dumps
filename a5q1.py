# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:29:39 2018

@author: Student
Assignment 5
1. Find a suitable value of k for a given dataset " CAR EVALUATION DATASET". Use the obtained K-value for developing KNN Classifier.
Report the classification accuracy.
"""

import csv #for importing csv data file
from helper_functions import pre_process_data
from helper_functions import k_nearest_neighbours,predict
#################


##################


#Read the CSV file into the python environment
data_list = []
with open('data.txt', 'rt') as csvfile:   
    read_obj = csv.reader(csvfile, delimiter = ',')
    for row in read_obj:
        data_list.append(row)
    #field_headings = data_list[0]
    #data_list.remove(data_list[0])
#print("Attribute headings are : ",field_headings)
complete_data = data_list

#PREPROCESSING DATA AND SHUFFLING
clean_data = pre_process_data(data_list)
import random
clean_data_shuffled = clean_data
random.shuffle(clean_data_shuffled)



TOTAL_RECORDS = len(clean_data)
TRAINING_SIZE = int(0.9 * TOTAL_RECORDS)
TESTING_SIZE = TOTAL_RECORDS - TRAINING_SIZE
print("TRAINING SIZE: ",TRAINING_SIZE, " TESTING SIZE : ",TESTING_SIZE)


#TESTING AND TRAINING DATA
training_data_list = clean_data_shuffled[0:TRAINING_SIZE]
testing_data_list = clean_data_shuffled[TRAINING_SIZE:TOTAL_RECORDS]
training_data = []
training_data_labels = []
for record in training_data_list:
    training_data.append(record[0:6])
    training_data_labels.append(record[6])
testing_data = []
testing_data_labels = []
for record in testing_data_list:
    testing_data.append(record[0:6])
    testing_data_labels.append(record[6])


error_matrix = []
for k in range(1,30):
    correct_classified = 0
    incorrect_classified = 0
    accuracy = 0
    for record,label in zip(testing_data,testing_data_labels):
        nearest_neighbours,labels = k_nearest_neighbours(record,k,training_data,training_data_labels)
        if(predict(record,nearest_neighbours,labels) == label):
            correct_classified = correct_classified + 1
            #print("S")
        else:
            incorrect_classified = incorrect_classified + 1
            #print("F")
    error = incorrect_classified / (correct_classified + incorrect_classified)
    error_matrix.append(error)
print(error_matrix)

import matplotlib.pyplot as plt
plt.plot(error_matrix)
