import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

np.set_printoptions(precision=2)

fruits = pd.read_table("../Week1/fruit_data_with_colors.txt")

feature_names_fruits = ["height", "width", "mass", "color_space"]
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']


target_names_fruits = ['apple', 'mandarin', 'orange', 'lemon']

