from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import json
import os
import numpy as np

# Read in dataset
X_train = np.genfromtxt("dataset/train_features.csv")
y_train = np.genfromtxt("dataset/train_labels.csv")
X_test = np.genfromtxt("dataset/test_features.csv")
y_test = np.genfromtxt("dataset/test_labels.csv")

# Fit a model
depth = 2
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
print(acc)
with open("metrics.json", "w") as outfile:
    outfile.write(json.dumps( {"Accuracy": str(acc)}))

# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize="true", cmap=plt.cm.Blues)
plt.savefig("plot.png")
