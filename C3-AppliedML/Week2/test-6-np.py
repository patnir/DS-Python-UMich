import numpy as np
import matplotlib.pyplot as plt

x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
a = np.append(x, y, axis=1)
print(np.shape(a))
print(x)
print(x.reshape(3, 2))

a = [[ 0.58554572,  0.56277696,  0.55473373],
     [ 0.91445428,  0.95125554,  0.92307692],
     [ 0.98967552,  0.99113737,  0.98816568],
     [ 1.        ,  1.        ,  1.        ],
     [ 0.98967552,  0.9985229 ,  0.99704142],
     [ 0.52212389,  0.52289513,  0.52218935]]


b = np.array([ 0.56647847,  0.93155951,  0.99039881,  1.        ,  1.        ,  1.        ])
c = np.array([ 0.56768547,  0.92959558,  0.98965952,  1.        ,  0.99507994,  0.52240279])

d = b - c


plt.figure()
plt.scatter(x, b, label="train data")
plt.scatter(x, c, label="test data")
plt.legend()
plt.show()
