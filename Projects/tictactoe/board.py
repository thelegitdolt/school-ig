from Projects.tictactoe.player import Player


class Square:
    ORD_A_MINUS_ONE = 64

    def __init__(self, position: str, state:bool=None):
        self.position = position
        self.state = state

    def __str__(self):
        return f'Square,{self.position},{self.get_symbol()}'

    def is_empty(self):
        return self.state is None

    def get_state(self):
        return self.state

    def get_position(self):
        return self.position

    def set_state(self, new_state):
        self.state = new_state

    def get_symbol(self):
        if self.state is None:
            return ' '
        elif self.state:
            return 'X'
        else:
            return 'O'

    def split_xy(self, convert_letter_to_number=False):
        a = [*self.position]
        return ord(a[0]) - Square.ORD_A_MINUS_ONE if convert_letter_to_number else a[0], int(a[1])



    def exists(self):
        if not len(self.position) == 2:
            return False
        letter, number = self.split_xy(True)
        if not 0 < letter < 4:
            return False
        if not 0 < number < 4:
            return False

        return True

    def to_number(self):
        if not self.exists():
            raise AttributeError(f'{self.position} is not a valid coordinate')

        letter, number = self.split_xy(convert_letter_to_number=True)

        if not 0 < letter < 4:
            raise AttributeError(f'{self.position} is not a valid coordinate')
        if not 0 < number < 4:
            raise AttributeError(f'{self.position} is not a valid coordinate')

        return 3 * (number - 1) + letter - 1

    def up(self):
        letter, number = self.split_xy()
        new = Square(f'{letter}{number - 1}')
        return new if new.exists() else None

    def down(self):
        letter, number = self.split_xy()
        new = Square(f'{letter}{number + 1}')
        return new if new.exists() else None

    def left(self):
        letter, number = self.split_xy(True)
        new = Square(f'{chr(letter - 1 + Square.ORD_A_MINUS_ONE)}{number}')
        return new if new.exists() else None

    def right(self):
        letter, number = self.split_xy(True)
        new = Square(f'{chr(letter + 1 + Square.ORD_A_MINUS_ONE)}{number}')
        return new if new.exists() else None

    @staticmethod
    def _checks_none(self, a, b):
        if (new_self := a(self)) is None:
            return None
        elif (newer_self := b(new_self)) is None:
            return None

        return newer_self

    def up_left(self):
        return Square._checks_none(self, Square.up, Square.left)

    def up_right(self):
        return Square._checks_none(self, Square.up, Square.right)

    def down_left(self):
        return Square._checks_none(self, Square.down, Square.left)

    def down_right(self):
        return Square._checks_none(self, Square.down, Square.right)




class Board:
    def __init__(self):
        self.last_turn_player = None
        self.board = [Square('A1'), Square('B1'), Square('C1'), Square('A2'), Square('B2'), Square('C2'), Square('A3'), Square('B3'), Square('C3')]

    def print_board(self):
        for i in self.board:
            print(i.__str__())

    # True is X, False is O, empty is None
    def set_board(self, pos: str, value: bool):
        posser = Square(pos)
        if not posser.exists():
            raise AttributeError(f"Cannot set; square {pos} does not exist")

        if not self.board[posser.to_number()].is_empty():
            raise AttributeError(f"Cannot set; square {pos} is full")

        self.board[posser.to_number()].set_state(value)
        return True

    def get_last_turn_player(self):
        return self.last_turn_player

    def set_last_turn_player(self, player: Player):
        self.last_turn_player = player

    def has_won(self, current_player: bool) -> bool:
        for square in self.board:
            if square.position == 'B2' or not square.get_state() == current_player:
                continue
            if self.check_victory_startpos(current_player, square):
                return True

        return False

    def check_victory_startpos(self, current_player: bool, start_pos: Square) -> bool:
        directions = (Square.up, Square.right, Square.left, Square.down, Square.up_left,
                      Square.up_right, Square.down_left, Square.down_right)

        good_directions = []


        for direction in directions:
            if (direct := direction(start_pos)) is None:
                continue

            actual_square = self.board[direct.to_number()]
            if not (actual_square.get_state() == current_player):
                continue

            good_directions.append(direction)

        for direction in good_directions:
            b = direction(start_pos)
            if (direct := direction(b)) is None:
                continue

            actual_square = self.board[direct.to_number()]
            if actual_square.get_state() == current_player:
                return True

        return False

    def has_tie(self):
        for square in self.board:
            if square.get_state() is None:
                return False

        return True

    def display_board(self):
        print(
            f"""
   A   B   C 
 +---+---+---+
1| %c | %c | %c |
 +---+---+---+
2| %c | %c | %c |
 +---+---+---+
3| %c | %c | %c |
 +---+---+---+
            """ % tuple(value.get_symbol() for value in self.board)
        )

    @staticmethod
    def preset_game(fen: str):
        a = Board()
        def uh_convert_ig(char):
            if char == 'X':
                return True
            elif char == ' ':
                return None
            else:
                return False

        def convert(blah_blah):
            a = blah_blah + 1
            if a == 1:
                return 'A1'
            elif a == 2:
                return 'A2'
            elif a == 3:
                return 'A3'
            elif a == 4:
                return 'B1'
            elif a == 5:
                return 'B2'
            elif a == 6:
                return 'B3'
            elif a == 7:
                return 'C1'
            elif a == 8:
                return 'C2'
            elif a == 9:
                return 'C3'
            return False
        a.board = [Square(convert(index), uh_convert_ig(char)) for index, char in enumerate([*fen])]
        return a

