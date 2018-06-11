from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
from sklearn import tree
from os import system

import sys
sys.path.insert(0, "/Users/rahulpatni/Projects/Coursera/DS-Python-UMich/C3-AppliedML/course3_downloads")

from adspy_shared_utilities import plot_decision_tree

scalar = MinMaxScaler()
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# X_train = scalar.fit_transform(X_train)
# X_test = scalar.fit_transform(X_test)

clf = DecisionTreeClassifier().fit(X_train, y_train)
print(clf.score(X_train, y_train))
print(clf.score(X_test, y_test))

clf2 = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)
print(clf2.score(X_train, y_train))
print(clf2.score(X_test, y_test))

plt.figure()
plot_decision_tree(clf, iris.feature_names, iris.target_names)
plt.show()