dataset = read.csv('Position_Salaries.csv')
dataset=dataset[2:3]
lin_reg =lm(formula = Salary ~ .,  data = dataset)
dataset$Level2 =dataset$Level^2
dataset$Level3 =dataset$Level^3
dataset$Level4 =dataset$Level^4
poly_reg =lm(formula = Salary ~ .,  data = dataset)



ggplot() +
  geom_point(aes(x=dataset$Level , y =dataset$Salary), colour= ' blue' )+
  geom_line(aes(x=dataset$Level , y = predict(lin_reg ,newdata = dataset)), colour= 'red')+
  ggtitle('Linear reg') +
  xlab('Level') + 
  ylab('Salary')

ggplot() + 
  geom_point(aes(x=dataset$Level , y =dataset$Salary), colour= ' blue' ) +
  geom_line(aes(x=dataset$Level , y = predict(poly_reg ,newdata = dataset)), colour= 'red' ) + 
  ggtitle('poly reg') 

y_pred = predict(poly_reg, data.frame(Level = 6.5,Level2 =6.5^2 , Level3 =6.5^3,Level4 =6.5^4))
