import random as rd
from time import sleep

class Player:
    def __init__(self, name, symbol):
        self.name = name
        from Projects.tictactoe.board import Square
        self.state = Square.symbol_to_bool(symbol)

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def get_sign(self):
        from Projects.tictactoe.board import Square

        return Square.symbol(self.state)

    def choose(self, board):
        from Projects.tictactoe.board import Square, Board

        input_string = f"{self.get_name()}, {Square('what', self.get_state()).get_symbol()}: Enter a cell [A-C][1-3]:"
        while True:
            coordinate = input(input_string).upper().replace(' ', '')
            if not (sqr := Square(coordinate)).in_bound():
                print("That's not a valid coordinate!")
                continue
            elif not board.get_board()[sqr.to_number()].is_empty():
                print("That grid is already taken!")
                continue
            break

        board.set_board(coordinate, self.get_state())


    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return (other.state == self.state) & (other.name == self.name)

class AI(Player):
    def __init__(self, name, state):
        super().__init__(name, state)

    def choose(self, board) -> str:
        sleep(0.5)
        print(f'{self.name} is choosing a move...')
        sleep(2)

        unfilled_spaces = [square.get_position() for square in board.get_board() if square.get_state() is None]
        board.set_board(unfilled_spaces[rd.randint(0, len(unfilled_spaces) - 1)], self.get_state())

class MinimaxAI(Player):

    def __init__(self, name, state):
        super().__init__(name, state)

    def choose(self, board) -> str:
        print(f'{self.name} is choosing a move...')
        sleep(0.5)
        board.set_board(MinimaxAI.mini_max(board, board.__copy__(), self.get_state(), True), self.get_state())

    @staticmethod
    def mini_max(board, starting_board, current_player: bool, should_return_moves):
        if (not should_return_moves) and not (res := board.get_result()) == 'c':
            if res == 't':
                return 0
            if res == 'X':
                return 1
            elif res == 'O':
                return -1

        max_score = -2
        min_score = 2

        possible_plays = []
        for square in board.get_board():
            if not square.is_empty():
                continue

            board.set_board(square.get_position(), current_player)
            score = MinimaxAI.mini_max(board.__copy__(), board, not current_player, False)

            board.replace_board(starting_board)

            if current_player:
                if score > max_score:
                    max_score = score
                    possible_plays.clear()
                if score >= max_score:
                    possible_plays.append(square.get_position())
            else:
                if score < min_score:
                    min_score = score
                    possible_plays.clear()
                if score <= min_score:
                    possible_plays.append(square.get_position())

        if should_return_moves:
            return possible_plays[rd.randint(0, len(possible_plays) - 1)]
        else:
            return max_score if current_player else min_score


class SmartAI(Player):
    def __init__(self, name, state):
        super().__init__(name, state)

    def choose(self, board) -> str:
        pass
