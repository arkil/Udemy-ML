# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 00:26:00 2018

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('E:/git/Udemy-ML/Logistic Regression/Social_Network_Ads.csv')
x = dataset.iloc[:, 2:3].values
y = dataset.iloc[:, 4].values

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.25 ,random_state= 0)


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train=sc_x.fit_transform(x_train) 
x_test = sc_x.transform(x_test)

from sklearn.linear_model import LogisticRegression

logReg = LogisticRegression(random_state = 0)
logReg.fit(x_train,y_train)

y_pred = logReg.predict(x_test)