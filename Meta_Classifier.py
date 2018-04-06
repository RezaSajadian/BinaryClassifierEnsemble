from BinaryClassifierEnsemble import instantiateValues, generateData
from sklearn.metrics import accuracy_score
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
    def __init__(self, seed, count, threshold):
        self.seed = seed
        self.count = count
        self.threshold = threshold
        self.classifiers = []

        for i in range(count):
            a1, b1, a2, b2, correlation = instantiateValues()
            self.classifiers.append(Classifier(a1, b1, a2, b2, self.seed, correlation))

    def classify(self, item):
        votes = []
        for classifier in self.classifiers:
            votes.append(classifier.classify(item))

        pos = 0
        neg = 0
        for vote in votes:
            if vote == 0:
                pos += 1
            else:
                neg += 1
        if pos / len(votes) >= self.threshold:
            return 1
        else:
            return 0


if __name__ == "__main__":

    giga = 1         #in case of grouping of metaClassifiers! which still doesn't change the result.
    count = 100000
    threshold = 0.5
    metas = []       #in case of grouping of metaClassifiers! which still doesn't change the result.
    for i in range(giga):
        a1, b1, a2, b2, correlation = instantiateValues()
        seed = Classifier(a1, b1, a2, b2, None, correlation)
        meta = MetaClassifier(seed, count, threshold)

    truth = generateData(70, 30)
    predict = []

    for item in truth:
        predict.append(meta.classify(item))

    print(accuracy_score(truth, predict))
