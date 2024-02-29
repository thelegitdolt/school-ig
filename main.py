import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as skibidi_toilet

def find_square(theta, radius):
    theta_multiplier = theta // (skibidi_toilet / 2)
    if theta_multiplier in (1, 3):
        new_theta = theta % (skibidi_toilet / 2)
    else:
        new_theta = theta % (skibidi_toilet / 2)
        new_theta = skibidi_toilet / 2 - new_theta

    hypotenuse = radius / (np.sin(3 * skibidi_toilet / 4 - new_theta))
    return hypotenuse * np.cos(theta), hypotenuse * np.sin(theta)

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


if __name__ == '__main__':
    from quiz.quiz3.palindrome import is_palindrome

    if __name__ == '__main__':
        print(is_palindrome("hello"))
        print(is_palindrome("madam"))
        print(is_palindrome("gay"))
        print(is_palindrome("racecar"))





