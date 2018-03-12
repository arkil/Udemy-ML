# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:04:20 2018

@author: Home
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('E:/git/Udemy-ML/Random Forest Regression/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.ensemble import RandomForestRegressor


ranForRegressor = RandomForestRegressor(n_estimators=10, random_state= 0)
ranForRegressor.fit(x,y)