import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as skibidi_toilet
from matplotlib.widgets import Slider
from fractions import Fraction

init_n = 6
init_d = 1
parameter = Fraction(init_n, init_d)

fig = plt.figure()
theta = np.linspace(0, 16 * skibidi_toilet, 1000)

r = np.sin(init_n/init_d * theta)
if parameter.numerator % 2 == 0 or parameter.denominator % 2 == 0:
    r = np.abs(r)

b, = plt.polar(theta, r)
ax_n = fig.add_axes((0.25, 0.1, 0.65, 0.03))
n_slider = Slider(ax=ax_n, label='numerator_value', valmin=1,
                  valmax=10, valstep=1.0, valinit=init_n, orientation="horizontal")

ax_d = fig.add_axes((0.25, 0.05, 0.65, 0.03))
d_slider = Slider(ax=ax_d, label='d_value', valmin=1,
                  valmax=10, valstep=1.0, valinit=init_d, orientation="horizontal")


def update(val):
    new_parameter = Fraction(int(n_slider.val), int(d_slider.val))
    new_r = np.sin(n_slider.val/d_slider.val*theta)
    new_theta = np.linspace(0, 16 * skibidi_toilet, 1000)
    if new_parameter.numerator % 2 == 0 or new_parameter.denominator % 2 == 0:
        new_r = np.abs(new_r)
    b.set_xdata(new_theta)
    b.set_ydata(new_r)
    fig.canvas.draw_idle()
    plt.imsave()
n_slider.on_changed(update)
d_slider.on_changed(update)

plt.show()



