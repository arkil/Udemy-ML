
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('50_Startups.csv')
x= dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,3]= labelencoder_x.fit_transform(x[:,3])
onehotencoder =OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()
x=x[:,1:]


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

pred_y =regressor.predict(X_test)

import statsmodels.formula.api as smf
x =np.append(arr = np.ones((50,1)).astype(int), values=x,axis=1)
x_opt = x[:,[0,1,2,3,4,5]]
regressor_ols =smf.OLS(endog =y ,exog =x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,1,3,4,5]]
regressor_ols =smf.OLS(endog =y ,exog =x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,3,4,5]]
regressor_ols =smf.OLS(endog =y ,exog =x_opt).fit()
regressor_ols.summary()
x_opt = x[:,[0,3,5]]
regressor_ols =smf.OLS(endog =y ,exog =x_opt).fit()
regressor_ols.summary()

x_opt = x[:,[0,3]]
regressor_ols =smf.OLS(endog =y ,exog =x_opt).fit()
regressor_ols.summary()




