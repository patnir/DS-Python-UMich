import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics.regression import r2_score

np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)


def part1_scatter(data, labels):
    plt.figure()
    plt.scatter(X_train, y_train, label='training data')
    plt.scatter(X_test, y_test, label='test data')
    for d in range(0, len(data)):
        plt.scatter(data[d][0], data[d][1], label=labels[d], s=4)
    plt.legend(loc=4)
    plt.show()


def get_linear_pred(x_s):
    model = LinearRegression()
    print(X_train)
    linreg = model.fit(X_train.reshape(-1, 1), y_train)
    new_ys = x_s * linreg.coef_[0] + linreg.intercept_
    return new_ys


def get_poly_pred(x_s, degree):
    poly = PolynomialFeatures(degree=degree)
    x_trans = poly.fit_transform(X_train.reshape(-1, 1))
    pred = poly.fit_transform(x_s.reshape(-1, 1))

    model = LinearRegression()
    model.fit(x_trans, y_train)
    return model.predict(pred)


def answer_one():
    new_xs = np.linspace(0, 10, 100)
    new_ys = get_linear_pred(new_xs)
    add_data = []
    labels = ["degree=1"]
    degrees=[3, 6, 9]
    ans = np.array([new_ys]).reshape(1, 100)
    for d in degrees:
        new_ys = get_poly_pred(new_xs, d)
        add_data.append([new_xs, new_ys])
        labels.append("degree=" + str(d))
        ans = np.vstack([ans, np.array([new_ys]).reshape(1, 100)])
    part1_scatter(add_data, labels)
    return ans



def plot_one(degree_predictions):
    plt.figure(figsize=(10,5))
    plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
    plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
    for i,degree in enumerate([1,3,6,9]):
        plt.plot(np.linspace(0,10,100), degree_predictions[i], alpha=0.8, lw=2, label='degree={}'.format(degree))
    plt.ylim(-1,2.5)
    plt.legend(loc=4)


def answer_two():
    degrees = range(0, 10)
    x_s = np.linspace(0, 10, 100)
    trains = []
    tests = []
    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        x_trans = poly.fit_transform(X_train.reshape(-1, 1))
        pred = poly.fit_transform(X_test.reshape(-1, 1))
        model = LinearRegression()
        model.fit(x_trans, y_train)
        y_pred = model.predict(x_trans)
        # print("degree: " + str(degree))
        r2_train = r2_score(y_train, y_pred)
        y_pred = model.predict(pred)
        r2_test = r2_score(y_test, y_pred)
        # print("train=" + str(r2_train) + " test= " + str(r2_test))
        curr_res = (r2_train, r2_test)
        trains.append(r2_train)
        tests.append(r2_test)

    res = (np.array(trains), np.array(tests))
    return res


def answer_three():
    rvals = answer_two()
    x = range(0, len(rvals[0]))
    diffs = rvals[0] - rvals[1]
    diffmax = diffs.argmin()  # Good_Generalization
    diffmin = diffs[diffmax + 1:].argmax() + diffmax + 1  # Overfitting
    diffmin2 = diffs[:diffmax].argmax()
    # plt.figure()
    # plt.scatter(x, rvals[0], label="train data")
    # plt.scatter(x, rvals[1], label="test data")
    # plt.legend()
    # plt.show()

    res = (diffmin2, diffmin, diffmax)
    return res  # Return your answer


def answer_four():
    degree = 12
    poly = PolynomialFeatures(degree=degree)
    x_fit = poly.fit_transform(X_train.reshape(-1, 1))
    x_test_fit = poly.fit_transform(X_test.reshape(-1, 1))
    model = LinearRegression()
    model.fit(x_fit, y_train)
    y_linear_pred = model.predict(x_test_fit)
    r_linear = r2_score(y_test, y_linear_pred)
    lasso = Lasso(alpha=0.01, max_iter=10000)
    lasso.fit(x_fit, y_train)
    y_lasso_pred = lasso.predict(x_test_fit)
    r_lasso = r2_score(y_test, y_lasso_pred)
    ans = (r_linear, r_lasso)
    return ans


