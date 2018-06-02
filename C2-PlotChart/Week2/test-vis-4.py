import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint

plt.figure()

linear_data = np.array([1, 2, 3, 4, 5, 6])
quadratic_data = linear_data**2
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)

new_xvals = []
for item in xvals:
    new_xvals.append(item + 0.3)

plt.bar(new_xvals, quadratic_data, width=0.3, color="red")

linear_err = [randint(0, 15) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, quadratic_data, width = 0.3, bottom=linear_data, color='r')

plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, quadratic_data, height = 0.3, left=linear_data, color='r')

plt.show()
