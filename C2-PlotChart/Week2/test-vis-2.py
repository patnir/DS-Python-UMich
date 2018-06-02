import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7])
y = x
plt.figure()
plt.scatter(x, y)

colors = ["green"]*(len(x) - 1)
colors.append("red")

plt.figure()
plt.scatter(x, y, s=100, c=colors)
# plt.show()

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# The single star * unpacks a collection into positional arguments
print(*zip_generator)

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
# let's turn the data back into 2 lists
x, y = zip(*zip_generator) # This is like calling zip((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))
print(x)
print(y)


plt.figure()
# plot a data series 'Tall students' in red using the first two elements of x and y
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students')
# plot a second data series 'Short students' in blue using the last three elements of x and y
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students')

# add a label to the x axis
plt.xlabel('The number of times the child kicked a ball')
# add a label to the y axis
plt.ylabel('The grade of the student')
# add a title
plt.title('Relationship between ball kicking and grades')

plt.legend(loc=4, frameon=False, title='Legend')


from matplotlib.artist import Artist

def rec_gc(art, depth = 0):
    if isinstance(art, Artist):
        print(" " * depth + str(art))
        for child in art.get_children():
            rec_gc(child, depth+2)

rec_gc(plt.legend())


