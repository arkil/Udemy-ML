

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('E:\git\Udemy-ML\Linear Regression lab\Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =1/3, random_state = 0)




from sklearn.linear_model import LinearRegression
abc = LinearRegression()
abc.fit(x_train,y_train)
predicty=abc.predict(x_test)

plt.scatter(x_train, y_train,color='red')
plt.plot(x_train,abc.predict(x_train),color='blue')
plt.title('salary vs experience')
plt.xlabel('salary')
plt.ylabel('experience')
plt.show()


plt.scatter(x_train, y_train,color='red')
plt.plot(x_train,abc.predict(x_train),color='blue')
plt.title('salary vs experience')
plt.xlabel('salary')
plt.ylabel('experience')
plt.show()

