import numpy as np
from numpy.random import uniform, seed 
from matplotlib import pyplot as plt
from matplotlib.mlab import griddata
import matplotlib.cm as cm

def iter_count(C, max_iter):
    X = C
    for n in range(max_iter):
        if abs(X) > 2.:
            return n
        X = X ** 2 + C
        return max_iter 
max_iter = 64
xmin, xmax, ymin, ymax = -2.2, .8, -1.5, 1.5
sample_count = 2 ** 12
A = uniform(xmin, xmax, sample_count)
B = uniform(ymin, ymax, sample_count)
C = [iter_count(complex(a, b), max_iter) for a, b in zip(A, B)]
N = 512
X = np.linspace(xmin, xmax, N)
Y = np.linspace(ymin, ymax, N)
Z = griddata(A, B, C, X, Y, interp = 'linear') 
plt.scatter(A, B, color = (0., 0., 0., .5), s = .5)
plt.imshow(Z,cmap = cm.binary,interpolation = 'bicubic',extent=(xmin, xmax, ymin, ymax))
plt.title("Non uniform data")

plt.show()   