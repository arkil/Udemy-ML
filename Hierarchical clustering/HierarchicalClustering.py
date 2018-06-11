# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 01:22:11 2018

@author: Home
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import scipy.cluster.hierarchy as sch
data=pd.read_csv("Mall_Customers.csv")

X = data.iloc[:,[3,4]].values 

dendrogram =sch.dendrogram(sch.linkage(X, method ='ward'))
plt.title('Dendrogram')
plt.xlabel('customers')
plt.ylabel('Euc Dist')
plt.show()


from sklearn.cluster import AgglomerativeClustering

hier_Clustering = AgglomerativeClustering(n_clusters=5 ,affinity ='euclidean',linkage = 'ward')

predict = hier_Clustering.fit_predict(X)

plt.scatter(X[predict == 0, 0], X[predict == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[predict == 1, 0], X[predict == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[predict == 2, 0], X[predict == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[predict == 3, 0], X[predict == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[predict == 4, 0], X[predict == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
