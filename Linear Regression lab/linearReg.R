dataset = read.csv('Salary_Data.csv')


library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

regressor =lm(formula = Salary ~ YearsExperience, data=training_set)

ypred = predict(regressor,newdata = test_set)
install.packages('ggplot2')

ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary),colour = 'blue' )+
  geom_line(aes(x=training_set$YearsExperience, y= predict(regressor,newdata =training_set)),colour = 'yellow' )+
  ggtitle('salary vs experience') +
xlab('Years of experience')+
ylab('Salary')
