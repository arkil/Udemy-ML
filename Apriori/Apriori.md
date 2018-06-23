# Apriori Association Rule Learning :


* It has Support, Confidence and Lift 
* Support(M) = num of users who watched movie M /total users
* Confidence(M1 -> M2) = num of users who watched movie M1 and M2 /total users watching M1
* lift(M1 -> M2) = confidence(M1 -> M2 ) /support (M2)


## steps ;

* Set a minimum support and confidence
* Take all subset in transaction having higher support than minimum 
* Take all the rules of subset having higher confidence than minimum confidence
* Sort the rules by decreasing lift

 