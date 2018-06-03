import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(1, 2, 1)
linear_data = np.array(range(5))
plt.plot(linear_data, "-o")

plt.subplot(1, 2, 2)
exponential_data = np.array(linear_data ** 2)
plt.plot(exponential_data, "-o")

plt.subplot(1, 2, 1)
plt.plot(exponential_data, "-x")

plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(linear_data, "-o")
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data, "-x")

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharex=True, sharey=True, )

ax5.plot(linear_data, '-')
ax7.plot(exponential_data, "-x")

# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

plt.gcf().canvas.draw()
plt.show()
