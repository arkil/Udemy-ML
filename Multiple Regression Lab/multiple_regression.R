dataset = read.csv('50_Startups.csv')
dataset$State = factor(dataset$State, levels =c('New York','California','florida'),labels =c(1,2,3) )

library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

##mlRegressor = lm(formula = Profit~ R.D.Spend + Administartion + Marketing.Spend + State)
mlRegressor = lm(formula = Profit ~ .,data = training_set)

y_pred = predict(mlRegressor,newdata=dataset)
