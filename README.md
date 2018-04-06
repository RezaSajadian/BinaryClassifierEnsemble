





Assignment 1 (1st part):



What is done in the existing program is as follows:

The goal is to create an ensemble of classifiers which is simulating a group of classifiers which are classifying an array of (item, label) data, and by means of an beta distribution, aiming to calculate the accuracy of the local machine's accuracy(mentioned as simulation) as the first pace, and test the process to create, predict, and provide the accuracy of the classification by a majority voting policy.

Classifiers are Beta classifiers which are receiving the alpha and beta arguments of the distribution by the machine's random number generation, and drawing instances from the Classifier class in done by means of a function which each time receives 6 input arguments, 4 arguments belonging to 2 beta distributions to generate classification results of beta functions for Positive and Negative default item classification accuracy of the classifier instance, one belonging to the classification result of a seed classifier(if any), and one argument representing the correlation of the existing classifier instance and the previous classifier's result. The function f is provoding us 2 values for negative and positive prediction accuracy, one value for the seed classifier's probability to be used, and one correlation value to define how the existing prediction is used in relation to the previous classifier's classification result.

The Classify function is the function which receives an item and a classifier, and performs the classification based on the generated probability of the item, to be whether a positive or negative item, and returns its prediction as a result, based on its beta distribution behavior.

Each time that the classify function runs, we generate the input values by the instantiateValues function, and compare them to the generated data(as the ground truth data, again randomly generated), and by each call of the classify function the result of one prediction is appended to an array called Votes.

The generateData function is planned to have certain number of negative and positive items, to have the desired proportion of the negative and positive items in our dataset, and also to be able to test the simulator for different scenarios of mainly negative items, or mainly positives.

This process is done once per each classifier call which is for each item, and in order to have the votes of the group of classifiers, we do this process for the demanded number of times(here 20 classification epochs, considering the natural phenomenon that the prediction accuracy converges raising the number of classifiers), and then based on a majority voting process, the vote of 20 classifiers are appended to an array called predict.

In order to judge the result of the classifier accuracy, the accuracy_score from the ScikitLearn library is providing the accuracy score of the ensemble per item, and for all the items in the dataset.



Results:

So, one schema is the proportion of 90% to 10% respectively belonging to Mainlypositive items, and just 10% negative items(positives as 1 and negatives as 0).
Another case is the test of the opposite case, to have mainly Negative items generated, and the minority belong to Positives, which by repeating the process, the result is not showing very reliable, But, as said previously, by raising the number of classifiers to high enough numbers(more than 5000), the result converges, and keeps steadily returning the manually set amount of 90%-10% or any other case intended.











########     Assignment 1 (2nd part)





This assignment is meant to present a metaClassifier which incorporates 
an n number of binary classifiers in an ensemble, and represent a prediction accuracy
based on a random argumented beta distribution.
Receiveing the voting Threshold of desire, and the number of classifiers representing, 
presents the expected voting as a classifier...







########      Assignment 1 (3rd part)

The 3rd part of the assignment 1 presents some changes to the previously presented meta classifier, which represented an ensemble of binary classifiers, but to investigate the results of the ensemble after setting different classifier precision, correlation and majority_voting threshold, and setting these amounts to see the changing behavior of the ensemble prediction accuracy, the results seem promising.

Changing the input to the distribution function for each individual classifier, the rest of the changes came through, and various scenarios were applied to the correlation amount setting, the input amount feeding of the seed classifier and the ensemble classifiers, and the proportion of the positive-negative items distribution in the grount-truth data.

The suggested number of classifiers in the ensemble was 10, which works acceptably fine, and raising this number to 30,
raises the sccuracy even better.







