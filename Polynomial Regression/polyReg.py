# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:19:09 2018

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:, 2].values


from sklearn.linear_model import LinearRegression

lReg =LinearRegression()
lReg.fit(x,y)


from sklearn.preprocessing import PolynomialFeatures
pReg = PolynomialFeatures(degree = 4)
x_poly = pReg.fit_transform(x)
pReg.fit(x_poly,y)
lReg2 = LinearRegression()
lReg2.fit(x_poly,y)

plt.scatter(x,y,color= 'blue')
plt.plot(x,lReg.predict(x), color='red')
plt.title('T vs F')
plt.show()

plt.scatter(x,y,color= 'blue')
plt.plot(x,lReg2.predict(pReg.fit_transform(x)), color='red')
plt.title('T vs F')
plt.show()

lReg.predict(6.5)

lReg2.predict(pReg.fit_transform(6.5))
