from Projects.tictactoe.good_tictactoe.player import Player


class Square:
    ORD_A_MINUS_ONE = 64

    def __init__(self, position: str, state: bool=None):
        self.position = position
        self.state = state

    def __str__(self):
        return f'Square,{self.position},{self.get_symbol()}'

    def __repr__(self):
        return f'Square({self.position}, {self.get_state()})'

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

    def in_bound(self):
        if not len(self.position) == 2:
            return False
        letter, number = self.split_xy(True)
        if not 0 < letter < 4:
            return False
        if not 0 < number < 4:
            return False

        return True

    def to_number(self):
        if not self.in_bound():
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
        return new if new.in_bound() else None

    def down(self):
        letter, number = self.split_xy()
        new = Square(f'{letter}{number + 1}')
        return new if new.in_bound() else None

    def left(self):
        letter, number = self.split_xy(True)
        new = Square(f'{chr(letter - 1 + Square.ORD_A_MINUS_ONE)}{number}')
        return new if new.in_bound() else None

    def right(self):
        letter, number = self.split_xy(True)
        new = Square(f'{chr(letter + 1 + Square.ORD_A_MINUS_ONE)}{number}')
        return new if new.in_bound() else None

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

    def get_board(self):
        return self.board

    # True is X, False is O, empty is None
    def set_board(self, pos: str, value: bool):
        posser = Square(pos)
        if not posser.in_bound():
            raise AttributeError(f"Cannot set; square {pos} does not exist")

        if not self.board[posser.to_number()].is_empty():
            raise AttributeError(f"Cannot set; square {pos} is full")

        self.board[posser.to_number()].set_state(value)
        return True

    def replace_board(self, other):
        self.board = [Square(i.get_position(), i.get_state()) for i in other.get_board()]

    def __copy__(self):
        copy = Board()
        copy.board = [Square(i.get_position(), i.get_state()) for i in self.get_board()]
        return copy

    def get_last_turn_player(self):
        return self.last_turn_player

    def set_last_turn_player(self, player: Player):
        self.last_turn_player = player

    # Returns 2 if X has won, 1 if O has won, 0 if there is a tie, and -1 if no victory
    def get_result(self) -> str:
        if len(a := self.check_victory()) == 1:
            return a
        elif self.check_tie():
            return 't'
        else:
            return 'c'

    def check_victory(self) -> str:
        for square in self.board:
            if square.position == 'B2':
                continue
            if len(victory := self.check_victory_startpos(square)) == 1:
                return victory

        return "None"

    # Returns 2 if X has won, 1 if O has won, 0 if no victory
    def check_victory_startpos(self, start_pos: Square) -> str:
        directions = (Square.up, Square.right, Square.left, Square.down, Square.up_left,
                      Square.up_right, Square.down_left, Square.down_right)

        good_directions = {}

        for direction in directions:
            if (direct := direction(start_pos)) is None:
                continue
            elif self.board[direct.to_number()].is_empty():
                continue

            actual_square = self.board[direct.to_number()]
            if not (actual_square.get_state() == start_pos.get_state()):
                continue

            good_directions[direction] = start_pos.get_state()

        for direction, state in good_directions.items():
            b = direction(start_pos)
            if (direct := direction(b)) is None:
                continue

            actual_square = self.board[direct.to_number()]
            if actual_square.get_state() == state:
                return 'X' if state else 'O'

        return "None"

    def check_tie(self):
        for square in self.board:
            if square.get_state() is None:
                return False

        return True

    def display_board(self, additional_message=' '):
        print(
            f"""{additional_message}
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

