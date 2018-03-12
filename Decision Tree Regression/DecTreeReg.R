
dataset = read.csv('Position_Salaries.csv')
dataset=dataset[2:3]

intsall.packages('rpart')

decTRegressor = rpart(formula = Salary ~ .,data=dataset, control = rpart.control(minsplit = 1))

y_pred = predict(decTRegressor, data.frame(Level = 6.5))

x_grid =seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot() + 
  geom_point(aes(x=dataset$Level , y =dataset$Salary), colour= ' blue' ) +
  geom_line(aes(x = x_grid , y = predict(decTRegressor , newdata =data.frame(Level=x_grid))), colour= 'red' ) + 
  ggtitle('Decison Tree Regressor ') 


