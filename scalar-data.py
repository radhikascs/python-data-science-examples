import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm 

n = 256
x = np.linspace(-3., 3., n)
y = np.linspace(-3., 3., n)
X, Y = np.meshgrid(x, y)

Z = X * np.sinc(X ** 2 + Y ** 2) 
plt.pcolormesh(X, Y, Z, cmap = cm.gray)
plt.title("Scalar data visualization")
plt.show() 