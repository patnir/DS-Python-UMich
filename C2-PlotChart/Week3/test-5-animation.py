import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

n = 100
x = np.random.randn(n)

fig = plt.figure()


def update(curr):
    if curr == n:
        a.event_source.stop()
    plt.cla()
    bins = np.arange(-4, 4, 0.25)
    plt.hist(x[:curr], bins=bins)
    plt.axis([-4, 4, 0, 30])
    plt.gca().set_title("Sampling the normal distribution")
    plt.gca().set_ylabel("Frequency")
    plt.gca().set_xlabel("Value")
    plt.annotate("n = {}".format(curr), [3, 27])


a = animation.FuncAnimation(fig, update, interval=100)

plt.show()
