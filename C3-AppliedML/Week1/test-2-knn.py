import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


fruits = pd.read_table('fruit_data_with_colors.txt')

lookup_fruit = dict(zip(fruits.fruit_label, fruits.fruit_name))
print(lookup_fruit)

X = fruits[["mass", "width", "height"]]
y = fruits["fruit_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)

print(knn.fit(X_train, y_train))

print(knn.score(X_test, y_test))

fruit_prediction = knn.predict([[20, 4.3, 5.5]])
print(fruit_prediction)
print(lookup_fruit[fruit_prediction[0]])

k_range = range(1, 20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))




plt.figure()
plt.scatter(k_range, scores)

plt.xticks([0,5,10,15,20])
plt.xlabel("k value")
plt.ylabel("accuracy")
plt.show()
