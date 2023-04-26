from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

# Define the apple dataset
# Each apple is represented by [color, texture, size] where 0 is unhealthy and 1 is healthy
apples = np.array([[1, 1, 1], [1, 1, 0], [0, 0, 0], [0, 1, 0], [1, 0, 1], [0, 1, 1], [1, 0, 0], [0, 0, 1]])
labels = np.array([1, 0, 0, 0, 1, 1, 0, 1])

# Split the dataset into a training set and a testing set
training_apples = apples[:6]
training_labels = labels[:6]
testing_apples = apples[6:]
testing_labels = labels[6:]

# Train a decision tree classifier on the training set
clf = tree.DecisionTreeClassifier()
clf.fit(training_apples, training_labels)

# Predict the labels for the testing set
predictions = clf.predict(testing_apples)

# Calculate the accuracy of the model
accuracy = accuracy_score(testing_labels, predictions)
print("Accuracy:", accuracy)
