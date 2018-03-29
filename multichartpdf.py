import numpy as np
from matplotlib import pyplot as plt

T = np.linspace(-np.pi, np.pi, 1024)
grid_size = (4,2)
plt.subplot2grid(grid_size,(0,0),rowspan=3, colspan=1)
plt.plot(np.sin(2*T),np.cos(0.5*T),c="k")
plt.subplot2grid(grid_size,(0,1),rowspan=3,colspan=1)
plt.plot(np.cos(3*T),np.cos(T),c="k")
plt.subplot2grid(grid_size,(3,0),rowspan=1,colspan=3)
plt.plot(np.sin(5*T),np.sin(7*T),c="k")
plt.tight_layout()
plt.savefig('Multigraphs in one pdf')
#plt.show()