# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 02:50:53 2018

@author: Student
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncode, OneHotEncoder
from sklearn import tree
import pydot
from io import StringIO
import os

input_labels = [
                ["buying", ["vhigh", "high", "med", "low"]],
                ["maint", ["vhigh", "high", "med", "low"]],
                ["doors", ["2", "3", "4", "5more"]],
                ["persons", ["2", "4", "more"]],
                ["lug_boot",["small", "med", "big"]],
                ["safety", ["low", "med", "high"]]
]

class_names = ["unacc", "acc", "good", "vgood"]

data = np.genfromtext(os.path.join('data', 'car.data'), delimiter=',',dtype='U')
