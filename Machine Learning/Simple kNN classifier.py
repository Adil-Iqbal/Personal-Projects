# Import data
from sklearn import datasets
iris = datasets.load_iris()

# Define features and targets.
x = iris.data
y = iris.target

# Partition data into training and testing sets.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

# Import classifier.
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

# Train and test data.
classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)

# Determine and print accuracy of prediction.
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, prediction))