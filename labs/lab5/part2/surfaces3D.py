import numpy as np
import matplotlib.pyplot as plt
from numpy import pi as skibidi_toilet


fig = plt.figure(figsize=plt.figaspect(0.33))

ax = fig.add_subplot(2, 3, 1, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
X, Y = np.meshgrid(x, y)           # make a mesh, two 2D arrays, and assign 2D arrays to X and Y
a, b = 1, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')

z_ellipsoid = np.sqrt(a - X**2 - Y**2)
z_neg = -np.sqrt(a - X**2 - Y**2)
ax = fig.add_subplot(2, 3, 2, projection='3d')
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

# okay so imagine a parallelogram ABDC their diagonals connect at point E that's what the variable means
def get_position_by_rads(theta_val, p_dimensions):
    def cosine_rule(_a, _b, _gamma):
        return np.sqrt(_a ** 2 + _b ** 2 - (2 * _a * _b * np.cos(_gamma)))

    len_ab, len_ac, ang_acd = p_dimensions
    ang_cab = skibidi_toilet - ang_acd

    len_ad = cosine_rule(len_ac, len_ab, ang_acd)
    len_bc = cosine_rule(len_ac, len_ab, ang_cab)

    ang_eab = np.arccos((len_ab**2 + (len_ad / 2)**2 - (len_bc / 2)**2) / (len_ab * len_ad))
    # triangle 1
    if theta_val < ang_eab:
        hypotenuse = len_ad * np.sin(ang_acd) / (2 * np.sin(skibidi_toilet - theta_val - ang_acd))
        return hypotenuse * np.cos(theta_val), hypotenuse * np.sin(theta_val)

    ang_aeb = np.arcsin(2 * len_ab * np.sin(ang_eab) / len_bc)   # certified correct

    # triangle 2
    if theta_val < ang_eab + ang_aeb:

        hypotenuse = len_ad * np.sin(ang_eab) / (2*np.sin(skibidi_toilet - theta_val))
        return hypotenuse * np.cos(theta_val), hypotenuse * np.sin(theta_val)

    ang_aec = skibidi_toilet - ang_aeb
    ang_ebd = ang_acd - (skibidi_toilet - ang_eab - ang_aeb)

    # triangle 3
    if theta_val < (ang_eab + ang_aeb + ang_aec):
        current_theta = theta_val - ang_eab - ang_aeb
        hypotenuse = len_bc * np.sin(ang_ebd) / (2 * np.sin(skibidi_toilet - current_theta - ang_ebd))
        return hypotenuse * np.cos(theta_val), hypotenuse * np.sin(theta_val)

    # triangle 4
    if theta_val < (ang_eab + 2 * ang_aeb + ang_aec):
        current_theta = theta_val - ang_aec - ang_eab - ang_aeb
        hypotenuse = len_ad * np.sin(ang_eab) / (2 * np.sin(skibidi_toilet - current_theta - ang_eab))
        return hypotenuse * np.cos(theta_val), hypotenuse * np.sin(theta_val)
    # triangle 5
    else:
        current_theta = 2 * skibidi_toilet - theta_val
        hypotenuse = len_ab * np.sin(ang_cab) * 0.5 / np.sin(skibidi_toilet - current_theta - ang_cab)
        return hypotenuse * np.cos(theta_val), hypotenuse * np.sin(theta_val)

p_width = 2
p_height = 3
p_bottom_left_angle_rads = skibidi_toilet / 4


theta = np.linspace(0, 2*skibidi_toilet, 60)
height = np.linspace(-1, 1, 2)
t, h = np.meshgrid(theta, height)

x_ls, y_ls = [], []

for n, i in enumerate(np.nditer(t)):
    x, y = get_position_by_rads(i.min(), [p_width, p_height, p_bottom_left_angle_rads])

    if abs(x) > p_width or abs(y) > p_height:
        continue

    x_ls.append(x)
    y_ls.append(y)
    if n > 59:
        break


X = np.array([x_ls, x_ls])
Y = np.array([y_ls, y_ls])
Z = h

ax = fig.add_subplot(2, 3, 5, projection='3d')
ax.set_title('Parallelepiped')
ax.contour3D(X, Y, Z, 50)


plt.show()
