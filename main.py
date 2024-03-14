import tkinter

import Projects.PA4.game

from tkinter import *
import tkinter.font as font

from Projects.PA4 import game

game.main()

# def change_text(event: tkinter.Event):
#     global message
#     pressed_button: tkinter.Button = event.widget
#     if message.get() == 'You clicked me!':
#         message.set('Click me again!')
#     else:
#         message.set('You clicked me!')
#
#
# # make a GUI window
# gui = Tk()
# message = StringVar()
# message.set('Click me')
# f = font.Font(family='Helveca', size='12', weight='bold')
# for x in range(4):
#     for y in range(4):
#         button = Button(textvariable=message, font=f, width=10, height=10, bg='bisque', fg='black')
#         button.bind('<Button-1>', change_text)
#         button.grid(row=y, column=x)
# mainloop()