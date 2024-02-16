import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=plt.figaspect(0.33))

ax = fig.add_subplot(2, 3, 1, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)           # make a mesh, two 2D arrays, and assign 2D arrays to X and Y
a,b = 1, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')

z_ellipsoid = np.sqrt(a - X**2 - Y**2)
z_neg = -np.sqrt(a - X**2 - Y**2)
ax = fig.add_subplot(2, 3, 2, projection='3d')
print(type(ax))
ax.set_title('Ellipsoid')
ax.contour3D(X, Y, z_ellipsoid, 25)
ax.contour3D(X, Y, z_neg, 25)

z_cone = -np.sqrt(X**2 + Y**2) + 1
ax = fig.add_subplot(2, 3, 3, projection='3d')
ax.set_title('cone')
ax.contour3D(X, Y, z_cone, 50)

ax = fig.add_subplot(2, 3, 4, projection='3d')
z_square_pyramid = -np.power((X**50/a + Y**50/b), 1/50) + 1
ax.set_title('Square Pyramid')
ax.contour3D(X, Y, z_square_pyramid, 50)
print(z_square_pyramid.size)
print(z_square_pyramid.shape)

ax = fig.add_subplot(2, 3, 5, projection='3d')
z_parallelogram = np.zeros((30, 30), dtype=float)
z_parallelogram[1:200:5,] = 50
# angle = 60
#
# edge_1 = np.array([a / 2 * np.cos(angle), a/2 + (a / 2 * np.sin(angle))])
# edge_2 = edge_1.copy()
# edge_2[0] -= b
# edge_3 = edge_1.copy()
# edge_3[0] -= a * np.cos(angle)
# edge_3[1] -= a * np.sin(angle)
# edge_4 = edge_2.copy()
# edge_4[0] -= a * np.cos(angle)
# edge_4[1] -= a * np.sin(angle)
#
# points_1st_layer = np.array([[edge_1[0] - (i/9) * (edge_1[0] - edge_2[0]), edge_1[1]] for i in range(1, 10)])


ax = fig.add_subplot(2, 3, 5, projection='3d')
ax.contour3D(X, Y, z_parallelogram, 50)

plt.show()
