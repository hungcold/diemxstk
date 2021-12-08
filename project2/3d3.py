import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

height = np.array([167,170,149,165,155,180,166,145,159,185,145,148,172,181,169])
weight = np.array([86,74,66,78,68,79,90,73,70,88,66,84,67,84,77])

plt.xlim(140,200)
plt.ylim(60,100)
plt.scatter(height,weight)
plt.title("Scatter Plot")
ax= plt.axes(projection='3d')
ax.plot3D(height,weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()