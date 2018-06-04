import matplotlib.pyplot as plt
import numpy as np

# dont use heatmaps for categorical data

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)

plt.figure()
plt.hist2d(X, Y, bins=25)
plt.colorbar()

plt.show()

