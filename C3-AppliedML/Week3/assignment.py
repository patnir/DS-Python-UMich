import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import recall_score, precision_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt

def answer_one():
    df = pd.read_csv("fraud_data.csv")
    return sum(df["Class"] == 1) / df.shape[0]


df = pd.read_csv("fraud_data.csv")
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


def answer_two():
    m = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    y_pred = m.predict(X_test)
    accuracy = m.score(X_test, y_test)
    recall = recall_score(y_test, y_pred)
    return accuracy, recall


def answer_three():
    svc = SVC().fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    accuracy = svc.score(X_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    return accuracy, recall, precision


def answer_four():
    svc = SVC(C=1e9, gamma=1e-07).fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    confusion = confusion_matrix(y_test, y_pred)
    return confusion


def answer_five():
    y_pred = LogisticRegression().fit(X_train, y_train).decision_function(X_test)
    # Your code here
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred)

    closest_zero = np.argmin(np.abs(thresholds))
    closest_zero_p = precision[closest_zero]
    closest_zero_r = recall[closest_zero]

    plt.figure()
    plt.xlim([0.0, 1.01])
    plt.ylim([0.0, 1.01])
    plt.plot(precision, recall, label='Precision-Recall Curve')
    plt.plot(closest_zero_p, closest_zero_r, 'o', markersize=12, fillstyle='none', c='r', mew=3)
    plt.xlabel('Precision', fontsize=16)
    plt.ylabel('Recall', fontsize=16)
    plt.axes().set_aspect('equal')

    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_pred)
    roc_auc_lr = auc(fpr_lr, tpr_lr)

    plt.figure()
    plt.xlim([-0.01, 1.00])
    plt.ylim([-0.01, 1.01])
    plt.plot(fpr_lr, tpr_lr, lw=3, label='LogRegr ROC curve (area = {:0.2f})'.format(roc_auc_lr))
    plt.xlabel('False Positive Rate', fontsize=16)
    plt.ylabel('True Positive Rate', fontsize=16)
    plt.title('ROC curve (1-of-10 digits classifier)', fontsize=16)
    plt.legend(loc='lower right', fontsize=13)
    plt.plot([0, 1], [0, 1], color='navy', lw=3, linestyle='--')
    plt.axes().set_aspect('equal')
    plt.show()

    print(precision)
    print(recall)
    print(fpr_lr)
    print(tpr_lr)

    return recall[np.where(precision == 0.75)][0], tpr_lr[np.where(fpr_lr >= 0.159)][0]


def answer_six():
    params = {'penalty': ['l1', 'l2'], 'C': [0.01, 0.1, 1, 10, 100]}
    m = LogisticRegression()
    grid = GridSearchCV(m, param_grid=params, scoring="recall")
    grid.fit(X_train, y_train)
    res = np.array(grid.cv_results_["mean_test_score"].reshape(5, 2))
    return res


# Use the following function to help visualize results from the grid search
def GridSearch_Heatmap(scores):

    plt.figure()
    sns.heatmap(scores.reshape(5,2), xticklabels=['l1','l2'], yticklabels=[0.01, 0.1, 1, 10, 100])
    plt.yticks(rotation=0);
    plt.show()

GridSearch_Heatmap(answer_six())

answer_six()
