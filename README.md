# BinaryClassifiersEnsemble
An Ensemble of Binary Classifiers


1. Generates binary classifiers:

This is a function that takes as input
- the parameters alfa and beta of a Beta distribution, representing a distribution of the classifier accuracy for negative items
- the parameters alfa and beta of a Beta distribution, representing a distribution of the classifier accuracy for positive items
- a seed classifier, that is, a classifier to which this classifier we are generating is correlated
- a correlation ( number in -1,1 range)
- a cost (a positive real number)

And in output generate the simulator of the classifier, that generates an object whose classify() function takes an input an item, and classifies it with an accuracy that depends on what has been generated


The classify() function works as follows:

- it gets the item to be classified (we know the true label for the item, so classify function simply simulate what the classifier, with the given accuracy, would generate when it receives an item with this label).
- it asks to the seed classifier, if any, to predict the class.
- it then predicts the class by itself, and it predicts correctly with a probability that depends on the accuracy value (which is different for true and false items)
- it then picks with probability [correlation] the value predicted by the seed (or it’s opposite, if the correlation is negative) and with 1-[correlation] it picks the value predicted by the classifier


2. We create a bunch of classifiers, and specifically, a list or array
So, we implement a function that given
i) again a beta distribution that describes where we see the distribution of classifiers to be,
ii) again a beta that picks a correlation value with the previous classifier (previous in the list)

Creates such array of classifiers


3. Now we have a bunch of classifiers.
We have a set of T <items, true label> in input, and our set of classifiers, and we want to:

A. measure the correlation among each pair of classifiers
B. filter classifiers that, after being tested in these T items, have a probability > P of having an accuracy lower than A. Then, use the remaining classifiers to make a prediction using i) majority voting, ii) weighted majority voting (where the weight is the accuracy of the classifiers as guessed from testing)
C. Use the data in T to build a model (initially, a linear regression) of the classifiers


Notice that because of the correlation, you have to compute each prediction of a classifier after you compute the previous one (regardless of whether we filter that classifier out)



