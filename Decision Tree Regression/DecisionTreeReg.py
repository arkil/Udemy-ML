# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:21:29 2018

@author: Home
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

from sklearn.tree import DecisionTreeRegressor
decisiontree_regressor =  DecisionTreeRegressor(random_state = 0)
decisiontree_regressor.fit(x,y)


y_pred = decisiontree_regressor.predict(6.5)