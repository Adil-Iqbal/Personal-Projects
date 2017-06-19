# Copyright 2017 by Adil Iqbal.
# All rights reserved.

"""Use k-Nearest Neighbors Algorithm to predict Iris dataset."""

from scipy.spatial import distance
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    """Build, train, & test kNN. Calculate & print accuracy."""
    iris = datasets.load_iris()
    x = iris.data  # Define features.
    y = iris.target  # Define targets.
    # Partition data into training and testing sets.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)
    classifier = Scrappy_kNN()  # Instantiate classifier.
    classifier.fit(x_train, y_train)  # Train classifier.
    prediction = classifier.predict(x_test)  # Test classifier.
    # Determine accuracy of predictions.
    result = accuracy_score(y_test, prediction)
    print(result)


def euc(a, b):
    """Return euclidean distance between a & b."""
    return distance.euclidean(a, b)


class Scrappy_kNN():
    """kNN classifier (k=1)."""

    def fit(self, x_train, y_train):
        """Memorize training data."""
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        """Build list of predictions."""
        predictions = []
        for row in x_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        """Find closest neighbor from training data."""
        best_dist = euc(row, self.x_train[0])
        best_index = 0
        for i, data in enumerate(self.x_train):
            dist = euc(row, data)
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


if __name__ == '__main__':
    main()
    exit()
