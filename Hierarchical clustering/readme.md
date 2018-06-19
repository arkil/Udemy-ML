# Hierarchical Clustering #

* Two types of Hierarchical Clustering
	* Agglomerative (bottom up approach)
	* Divisive(top down)
	
* Make each data point a single point cluster(forming N cluster)
* take two closest data point and make one cluster(forming N-1 cluster)
* take two closest cluster and make one cluster(forming N-2 cluster)
* repeat until to form one cluster  

## Dendograms ##

* Dendograms are tree diagram used to illustrate the arrangement of the clusters produced by hierarchical clustering
* In dendograms , dissimilarity shoud be less than threshold 
	