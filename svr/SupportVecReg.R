install.packages('e1071')
dataset = read.csv('Position_Salaries.csv')
dataset=dataset[2:3]

svr =svm(formula = Salary ~ .,data=dataset, type = 'eps-regression')



y_pred = predict(poly_reg, data.frame(Level = 6.5))


ggplot() + 
  geom_point(aes(x=dataset$Level , y =dataset$Salary), colour= ' blue' ) +
  geom_line(aes(x=dataset$Level , y = predict(svr ,newdata = dataset)), colour= 'red' ) + 
  ggtitle('SVR ') 



