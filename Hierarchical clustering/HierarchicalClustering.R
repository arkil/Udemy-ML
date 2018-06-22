library(cluster)
dataset = read.csv("Mall_Customers.csv")

X = dataset[4:5]

dendogram = hclust(dist(X,method = "euclidean"),method = 'ward.D')

plot(dendogram, main = paste('Dendogram'), xlab = 'customers', ylab = 'Euclidean Distances')

y_hc = cutree(dendogram, 5)


clusplot(X, y_hc, lines=0, shade=TRUE,color=TRUE,plotchar = FALSE, span=TRUE, labels=2, main=paste('Cluster'),xlab='Income',ylab='Spending power')