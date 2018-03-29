import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(0, 2 * np.pi, 8)
points = np.vstack((np.cos(theta), np.sin(theta))).transpose()
plt.figure(figsize=(4., 4.))
plt.gca().add_patch(plt.Polygon(points, color = '.75'))
plt.grid(True)
plt.axis('scaled')
plt.title("Polygon Repesentation")
plt.savefig('polygon.pdf')
#plt.show()