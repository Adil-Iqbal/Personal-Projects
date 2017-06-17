from scipy.spatial import distance
def euc(a, b):
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
        return y_train[best_index]

# Import data
from sklearn import datasets
iris = datasets.load_iris()

# Define features and targets.
x = iris.data
y = iris.target

# Partition data into training and testing sets.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

# Instantiate classifier.
classifier = Scrappy_kNN()

# Train and test data.
classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)

# Determine accuracy of predictions.
from sklearn.metrics import accuracy_score
result = accuracy_score(y_test, prediction)

# Print accuracy of predictions.
print(result)
