import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as skibidi_toilet

def pyramid(base_sides, height):
    base_points = []
    radius = 2
    thetas = np.linspace(0, 2 * skibidi_toilet, base_sides + 1)

    for theta in np.nditer(thetas):
        base_points.append([radius * np.cos(theta), radius * np.sin(theta)])

    base_points = np.array(base_points)
    x = np.array([base_points[:, 0].tolist(), [0 for _ in range(base_sides + 1)]])
    y = np.array([base_points[:, 1].tolist(), [0 for _ in range(base_sides + 1)]])
    z = np.array([[0 for _ in range(base_sides + 1)], [height for _ in range(base_sides + 1)]])

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.contour3D(x, y, z, 50)

    plt.show()
