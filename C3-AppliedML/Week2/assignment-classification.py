import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

mush_df = pd.read_csv("mushrooms.csv")
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:, 2:]
y_mush = mush_df2.iloc[:, 1]

X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)

X_subset = X_test2
y_subset = y_test2


def answer_five():
    clf = DecisionTreeClassifier()
    a = clf.fit(X_train2, y_train2)
    features = pd.Series(data=a.feature_importances_, index=X_train2.columns)
    features = features.sort_values(ascending=False)
    return list(features[0:5].index)


def answer_six():
    gamma = np.logspace(-4,1,6)
    svc = SVC(random_state=0, kernel="rbf", C=1)
    trainscore, testscore = validation_curve(estimator=svc, X=X_subset, y=y_subset, scoring="accuracy", param_name="gamma", param_range=gamma)
    # Your code here
    ans = (np.average(trainscore, axis=1), np.average(testscore, axis=1))
    return ans


print(answer_six())
