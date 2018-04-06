
from BinaryClassifierEnsemble import generateData
from sklearn.metrics import accuracy_score, confusion_matrix
from scipy.stats import beta
import random


class Classifier(object):
    def __init__(self, a1, b1, a2, b2, seed, correlation):
        self.positiveAcc = beta.rvs(a1, b1, size=1)
        self.negativeAcc = beta.rvs(a2, b2, size=1)
        self.seed = seed
        self.correlation = correlation

    def classify(self, item):
        if self.seed is not None:
            rand = random.random()
            if rand < self.correlation:
                seedPrediction = seed.classify(item)
                return seedPrediction

        if item == 1:
            accuracy = self.positiveAcc
            rand = random.random()
            if rand > accuracy:
                return 0
            else:
                return 1
        elif item == 0:
            accuracy = self.negativeAcc
            rand = random.random()
            if rand > accuracy:
                return 1
            else:
                return 0


class MetaClassifier(object):
    def __init__(self, seed, count, threshold, a1, b1, a2, b2, correlation):
        self.seed = seed
        self.count = count
        self.threshold = threshold
        self.classifiers = []
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
        self.correlation = correlation

        for i in range(count):
            self.classifiers.append(Classifier(self.a1, self.b1,
                                               self.a2, self.b2,
                                               self.seed, self.correlation))

    def classify(self, item):
        votes = []
        for classifier in self.classifiers:
            votes.append(classifier.classify(item))

        pos = 0
        neg = 0
        for vote in votes:
            if vote == 0:
                neg += 1
            else:
                pos += 1
        if pos / len(votes) >= self.threshold:
            return 1
        else:
            return 0


if __name__ == "__main__":

    count = 10
    threshold = 0.475

    a1, b1, a2, b2 = 1000, 10, 1000, 10
    seed = Classifier(a1, b1, a2, b2, None, None)
    #print(seed.negativeAcc, seed.positiveAcc)

    a1, b1, a2, b2, correlation = 1000, 1000, 1000, 1000, 0.5
    meta = MetaClassifier(seed, count, threshold, a1, b1, a2, b2, correlation)

    # for classifier in meta.classifiers:
    #     print(classifier.negativeAcc, classifier.positiveAcc, classifier.correlation)

    truth = generateData(75, 25)
    predict = []

    for item in truth:
        predict.append(meta.classify(item))

    print(accuracy_score(truth, predict))
    print(confusion_matrix(truth, predict))




