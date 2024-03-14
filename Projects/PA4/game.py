import tkinter.font as font
from tkinter import *

from Projects.PA4.fifteen import Fifteen

def main():
    def get_event_handler_for_key(pos):
        def handler():
            board_state = board.square_search()
            # check if move is like, actually legal, like can you like actually make the move
            if board.update(board_state[pos]):
                # get new board
                board_state = board.square_search()
                # Update the board
                for ind, msg in enumerate(labels):
                    labels[ind].set(board_state[ind] if board_state[ind] != 16 else ' ')
                    
                # updates solved message if the board is solved
                if board.is_solved():
                    finished_message.set('Solved!')
                # un-updates solved message when the board is un-solved somehow like when you scrambled it
                elif finished_message.get() == 'Solved!':
                    finished_message.set('')
        return handler
    
    # what happens after you press shuffle
    def shuffle():
        # do the. do the shuffle
        board.shuffle()
        # get the new board state
        board_state = board.square_search()
        # update the board
        for ind, msg in enumerate(labels):
            labels[ind].set(board_state[ind] if board_state[ind] != 16 else ' ')
            
        # JUST IN CASE you somehow managed to solve it by shuffling
        if board.is_solved():
            finished_message.set('Solved!')
        # marks the puzzle unsolved after shuffling
        else:
            if finished_message.get() == 'Solved!':
                finished_message.set('')
            
    
    def add_button(current_gui, value, pos, _font, after):
        # value is tile label,
        # pos is position on board, goes from 0 to 15
        return Button(current_gui, textvariable=value, name=str(pos),
                      font=_font, height=2, width=5, bg='white', fg='black',
                      command=after)
    
    # Fifteen
    board = Fifteen()
    
    # Interface beautification
    gui = Tk()
    gui.title('Fifteen Game Made By Andrew')
    game_font = font.Font(family='Helveca', size=25, weight='bold')
    labels = [StringVar() for _ in range(16)]
    
    buttons = []
    for i in range(16):
        if i != 15:
            labels[i].set(str(i + 1))
        else:
            labels[i].set('')
        button = add_button(gui, value=labels[i], pos=i, _font=game_font, after=get_event_handler_for_key(i))
        buttons.append(button)
        button.grid(row=i // 4 + 1, column=i % 4 + 1)
    
    # thing that tells you whether you've solved the thing or not.
    finished_message = StringVar()
    is_solved_button = add_button(gui, value=finished_message, pos=17, _font=game_font, after=lambda: None)
    is_solved_button.grid(row=5, column=3)
    
    # shuffle button, it's at the bottom left
    shuffle_msg = StringVar()
    shuffle_msg.set('Scramble')
    game_font = font.Font(family='Helveca', size=20, weight='bold')
    shuffle_button = add_button(gui, value=shuffle_msg, pos=18, _font=game_font, after=shuffle)
    shuffle_button.grid(row=5, column=2)
    
    # Main Loop
    mainloop()
