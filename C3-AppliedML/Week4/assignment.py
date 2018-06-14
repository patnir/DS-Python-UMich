import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, accuracy_score, precision_score
from sklearn.metrics import roc_curve, auc
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor

scaler = MinMaxScaler()
train = pd.read_csv("train.csv", encoding="ISO-8859-1")
test = pd.read_csv("test.csv", encoding="ISO-8859-1")


for c in test.columns:
    if len(test[c].unique()) < 10 and len(test[c].unique()) > 2:
        i = 0

        uni_values = list(set(test[c].unique()) | set(train[c].unique()))
        print(uni_values)

        for label in uni_values:
            test[c][test[c] == label] = np.float64(i)
            train[c][train[c] == label] = np.float64(i)
            i += 1

        test[c] = test[c].astype(np.float64)
        train[c] = train[c].astype(np.float64)

print(test.dtypes)

train = train.set_index(["ticket_id"])
test = test.set_index(["ticket_id"])
test = test.drop("non_us_str_code", axis=1)

test = test.select_dtypes(include=[np.float64])

for col in test.columns:
    test[col].replace(to_replace=np.NaN, value=np.nanmedian(np.float64(test[col])))
    test[col] = np.nan_to_num(test[col])

compliance = train["compliance"]
train = train[test.columns]
train["compliance"] = compliance
train = train.select_dtypes(include=[np.float64])
train = train[(train["compliance"] == 1) | (train["compliance"] == 0)]

for col in train.columns:
    train[col].replace(to_replace=np.NaN, value=np.nanmedian(np.float64(train[col])))
    train[col] = np.nan_to_num(train[col])

X = train.iloc[:, :-1]
y = train.iloc[:, -1]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
test_scaled = scaler.transform(test)


def print_stats(y_test, y_prediction):
    print("accuracy  = {}".format(accuracy_score(y_test, y_prediction)))
    print("recall    = {}".format(recall_score(y_test, y_prediction)))
    print("precision = {}".format(precision_score(y_test, y_prediction)))
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prediction)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    print("auc       = {}\n".format(roc_auc_lr))


def blight_model():
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_prediction = model.predict(X_test)

    y_prediction_abs = np.float64(y_prediction >= 0.5)

    print_stats(y_test, y_prediction_abs)

    return pd.Series(data=model.predict(test), index=test.index, name="compliance")


print(blight_model())
