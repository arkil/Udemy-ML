# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:25:43 2018

@author: Home
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

from sklearn.svm import SVR
svr = SVR(kernel = 'rbf')
svr.fit(x,y)

y_pred = svr.predict(6.5)
y_pred = sc_y.inverse_transform(y_pred)


plt.scatter(x,y,color= 'blue')
plt.plot(x,svr.predict(x), color='red')
plt.title('T vs F')
plt.show()


