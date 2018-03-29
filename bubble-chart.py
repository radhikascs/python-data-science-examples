import matplotlib.pyplot as plt
import numpy as np

#create data
x = np.random.rand(5)
y = np.random.rand(5)
z = np.random.rand(5)

#Change color with c and alpha
plt.title("Bubble chart demonstration")
plt.scatter(x,y,s=z*4000, c="red", alpha=0.4)
plt.show()