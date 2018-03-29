import matplotlib.pyplot as plt
import numpy as np

XY = np.random.rand(10,2,3)

labels = ['test1', 'test2', 'test3']
colors = ['r','b','g']

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(8, 6))
    ax = plt.gca()

    i=0
    for lab,col in zip(labels, colors):
        ax.scatter(XY[:,0,i],XY[:,1,i],label=lab, c=col)
        i+=1

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Clustering values of Test Results')
    plt.legend(loc='lower center')
    plt.tight_layout()
    plt.show()