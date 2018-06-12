import numpy as np
x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
a = np.append(x, y, axis=1)
print(np.shape(a))
print(x)
print(x.reshape(3, 2))