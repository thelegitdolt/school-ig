from tkinter import *

from PIL import Image

fname = '/Users/andrewyinschool/Desktop/code/ssshishihps/Projects/PA2/plant.gif'
gif = Image.open(fname)
frames = []

root = Tk()
root.geometry("350x200")
root.title("The Plant Gif (it's funny)")

for i in range(gif.n_frames):
    frames.append(PhotoImage(file=fname, format=f"gif -index {i}"))  # create a list of frames

label = Label(root)
label.pack()

def play_animation(num):

    img = frames[num]
    label.configure(image=img)
    new_num = num + 1 if num < 7 else 0

    label.after(100, lambda: play_animation(new_num))

# play_animation(0)
play_animation(0)
root.mainloop()
