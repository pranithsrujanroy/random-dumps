# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 01:58:14 2018

@author: Pranith Srujan Roy M
"""

import csv

age = 0
count = 0
with open('patient_data.csv', 'rb') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1]  and row[1]!='Age':
            print(row[1])
            age = age + int(row[1])
            count = count+1
age = age/count
file1 = open('patient_data.csv', 'rb')
reader = csv.reader(file1)
new_rows_list = []
for row in reader:
    if row[2]=='male':
        row[2] = '0'
    elif row[2]=='female':
        row[2] = '1'
    if row[4] == 'TRUE':
        row[4] = '1'
    elif row[4] == 'FALSE':
        row[4] = '0'
    if row[1]=='':
        row[1] = age
    new_rows_list.append(row)
    print(row)
file1.close()

file2 = open('patient_data.csv', 'wb')
writer = csv.writer(file2)
writer.writerows(new_rows_list)
file2.close()

l = []
tumor_size_null = []
with open('patient_data.csv','rb') as file:
    reader = csv.reader(file)
    for row in reader:
        if not row[3]:
            tumor_size_null.append(row)
print(tumor_size_null)

with open('patient_data.csv','rb') as file:
    reader = csv.reader(file)
    for item in tumor_size_null:
        tumor_size = 0
        count_same = 0
        for row in reader:
            print('hi')
            if item[0]!=row[0] and item[1] == row[1]:
                print('hi')
                tumor_size += float(row[3])
                count_same += 1
            if item[0]!=row[0]:
                l.append(row)
        if count_same!=0:
            item[3] = str(tumor_size/count_same)
        l.append(item)
print(l)

with open('patient_data.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerows(l)