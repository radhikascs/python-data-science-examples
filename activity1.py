# Import the library

import matplotlib.pyplot as plt

values = [82,75,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,32]
plt.hist(values,5, histtype='bar', align='mid',color='c',label='Test Score Data',edgecolor='black')
plt.legend()
plt.title('Histogram of score')
plt.show()
