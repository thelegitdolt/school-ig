import math
import time
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('Sine Wave Yay!')
#  analysis!!!!!!!

# np.argmax(x) == max(y)

max_y = max(y)
max_index = np.where(y == max(y)[0][0])
max_arg_x = x[max_index]

arg_max = x[np.argmax(y)]



canvas=Tk()
canvas.title("Digital Clock")
canvas.geometry("350x200")
label = Label(canvas, font=("courier"), )
def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


