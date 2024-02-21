import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')
theta = np.linspace(0, 2*np.pi, 30)
height = np.linspace(-1, 1, 2)
t, h = np.meshgrid(theta, height)   # make a mesh, two 2D arrays
radius = 1
X = radius * np.cos(t)
Y = radius * np.sin(t)
Z = h
print(Z)
ax.contour3D(X, Y, Z, 50)
ax.set_title('Cylinder')
plt.show()