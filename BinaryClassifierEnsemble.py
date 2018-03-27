from scipy.stats import beta
from sklearn.metrics import accuracy_score
import random


class Classifier(object):
    def __init__(self, positiveAcc, negativeAcc, seed, correlation):
        self.positiveAcc = positiveAcc
        self.negativeAcc = negativeAcc
        self.seed = seed
        self.correlation = correlation


def f(a1, b1, a2, b2, seed, correlation):
    acForPositive = beta.rvs(a1, b1, size=1)
    acForNegative = beta.rvs(a2, b2, size=1)

    classifier = Classifier(acForPositive, acForNegative, seed, correlation)

    return classifier


def classify(item, classifier):
    if classifier.seed is not None:
        rand = random.random()
        if rand < classifier.correlation:
            seedPrediction = classify(item, classifier.seed)
            return seedPrediction

    if item == 1:
        accuracy = classifier.positiveAcc
        rand = random.random()
        if rand > accuracy:
            return 0
        else:
            return 1
    elif item == 0:
        accuracy = classifier.negativeAcc
        rand = random.random()
        if rand > accuracy:
            return 1
        else:
            return 0


def instantiateValues():
    a1 = random.random()
    b1 = random.random()
    a2 = random.random()
    b2 = random.random()
    correlation = random.random()
    return a1, b1, a2, b2, correlation


def generateData(pos, neg):
    data = []
    for i in range(neg):
        data.append(0)
    for i in range(pos):
        data.append(1)
    return data

def majority_voting(votes):
    pos = 0
    neg = 0
    for vote in votes:
        if vote == 0:
            pos += 1
        else:
            neg += 1

    if pos >= neg:
        return 1
    else:
        return 0


if __name__ == "__main__":

    truth = generateData(90, 10)
    predict = []

    a1, b1, a2, b2, correlation = instantiateValues()
    seed = f(a1, b1, a2, b2, None, correlation)
    classifiers = []

    for i in range(0, 20):
        a1, b1, a2, b2, correlation = instantiateValues()
        classifiers.append(f(a1, b1, a2, b2, seed, correlation))

    for item in truth:
        votes = []
        for classifier in classifiers:
            votes.append(classify(item, classifier))
        predicted = majority_voting(votes)
        predict.append(predicted)


    print(accuracy_score(truth, predict))

