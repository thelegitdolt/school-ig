import random as rd
from time import sleep

class Player:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def choose(self, board) -> str:
        from Projects.tictactoe.board import Square

        input_string = f"{self.get_name()}, {Square('what', self.get_state()).get_symbol()}: Enter a cell [A-C][1-3]:"
        while True:
            coordinate = input(input_string)
            if not (sqr := Square(coordinate)).in_bound():
                print("That's not a valid coordinate!")
                continue
            elif not board.get_board()[sqr.to_number()].is_empty():
                print("That grid is already taken!")
                continue
            break

        return coordinate


    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return (other.state == self.state) & (other.name == self.name)

class RandomAI(Player):
    def __init__(self, name, state):
        super().__init__(name, state)

    def choose(self, board) -> str:
        sleep(0.5)
        print(f'{self.name} is choosing a move...')
        sleep(2)

        unfilled_spaces = [square.get_position() for square in board.get_board() if square.get_state() is None]

        return unfilled_spaces[rd.randint(0, len(unfilled_spaces) - 1)]

class MinimaxAI(Player):
    def __init__(self, name, state):
        super().__init__(name, state)

    def choose(self, board) -> str:
        raise NotImplementedError

