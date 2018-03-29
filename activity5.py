import numpy as np
import matplotlib.pyplot as plt

#Generate random normally distributed data
data = np.random.randn(10000)

#Plotting the histogram
heights,bins = np.histogram(data,bins=50)

#Normalizing the curve
heights = heights/float(sum(heights))
binMinds = bins[:-1]+np.diff(bins)/2
plt.plot(binMinds,heights)
plt.title("Probability Distribution")
plt.show()