import numpy as np
from matplotlib import pyplot as plt

X = np.linspace(-10,10,1024)
Y = np.sinc(X)

plt.plot(X,Y)
plt.show()
plt.savefig('sinc.png',c='k')
