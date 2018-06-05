import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0, 10, 1000), name="v1")
v2 = pd.Series(2*v1 + np.random.normal(60,15,1000), name="v2")

plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label="v1")
plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label="v1")
plt.legend()

plt.figure()
plt.hist([v1, v2], histtype="barstacked", normed=True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3)

plt.figure()
sns.distplot(v3, hist_kws={"color": "Teal"}, kde_kws={"color": "Navy"})

sns.jointplot(v1, v2, alpha=0.7)

grid = sns.jointplot(v1, v2, alpha=0.4)
grid.ax_joint.set_aspect("equal")

sns.jointplot(v1, v2, kind="hex")

sns.set_style("white")
sns.jointplot(v1, v2, kind="kde", space=0)

irispath = "/Users/rahulpatni/Projects/Coursera/DS-Python-UMich/C2-PlotChart/Week4/iris.csv"

iris = pd.read_csv(irispath)

sns.pairplot(iris, hue="Name", diag_kind="kde", size=2)

plt.figure(figsize=(12, 8))
plt.subplot(121)
sns.swarmplot("Name", "PetalLength", data=iris)
plt.subplot(122)
sns.violinplot("Name", "PetalLength", data=iris)

plt.show()
