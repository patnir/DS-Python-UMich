import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import cm
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table("fruit_data_with_colors.txt")

X = fruits[["mass", "width", "height", "fruit_label", "color_score"]]
Y = fruits["fruit_label"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

# random state = provides seed value, will result in different randomized splits

fruit_names = dict(zip(fruits["fruit_label"].unique(), fruits.fruit_name.unique()))
print(fruit_names)

cmap = cm.get_cmap("gnuplot")
scatter = pd.scatter_matrix(X_train, c=y_train, marker="o", s=40, hist_kwds={"bins": 15}, figsize=(9,9), cmap=cmap)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X_train["width"], X_train["height"], X_train["color_score"], c=y_train, marker="o", s=100)
ax.set_xlabel("width")
ax.set_ylabel("height")
ax.set_zlabel("color_score")

plt.show()
