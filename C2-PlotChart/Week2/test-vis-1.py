import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

print(mpl.get_backend())

plt.plot(3, 2, ".")

fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.add_subplot(111)
ax.plot(3, 2, ".")
canvas.print_png("test.png")

plt.figure()
plt.plot(3, 2, "o")
ax = plt.gca()
print(ax.axis([0, 6, 0, 10]))

plt.figure()
plt.plot(1.5, 1.5, "o")
plt.plot(2.5, 1.5, "o")
plt.plot(4.5, 1.5, "o")

plt.show()

ax = plt.gca()
print(ax.get_children())


