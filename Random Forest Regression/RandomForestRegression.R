install.packages('randomForest')

dataset = read.csv('Position_Salaries.csv')
dataset=dataset[2:3]

set.seed(1234)
ranForReg =randomForest(x=dataset[1],y=dataset$Salary, ntree = 500 )
y_pred = predict(ranForReg, data.frame(Level = 6.5))


x_grid =seq(min(dataset$Level),max(dataset$Level),0.01)
ggplot() + 
  geom_point(aes(x=dataset$Level , y =dataset$Salary), colour= ' blue' ) +
  geom_line(aes(x = x_grid , y = predict(ranForReg , newdata =data.frame(Level=x_grid))), colour= 'red' ) + 
  ggtitle('Random forest Regressor ') 
