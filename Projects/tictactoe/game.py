from Projects.tictactoe.board import Board, Square
from Projects.tictactoe.player import Player

def init():
    print("Welcome to TIC-TAC-TOE Game!")
    board = Board()

    player1 = Player('Bob', True)
    player2 = Player('Alice', False)


    while True:
        result = turn(player1, player2, board)
        if result == 1:
            board.display_board()
            print(f"{board.get_last_turn_player().get_name()} is a winner!")
            break
        elif result == 2:
            board.display_board()
            print("It is a tie!")
            break

    while True:
        replay = input('Would you like to play again? [Y/N]')
        if replay == 'y' or replay == 'Y':
            init()
            break
        elif replay == 'n' or replay == 'N':
            print("Goodbye!")
            break
        else:
            print("Invalid answer!")

def turn(player1: Player, player2: Player, board: Board):
    if (last_player := board.get_last_turn_player()) is None or last_player == player2:
        current_player = player1
    else:
        current_player = player2

    board.display_board()

    input_string = f"{current_player.get_name()}, {Square('what', current_player.get_state()).get_symbol()}: Enter a cell [A-C][1-3]:"
    coordinate = input(input_string)

    while not Square(coordinate).exists():
        print("That's not a valid coordinate!")
        coordinate = input(input_string)

    board.set_board(coordinate, current_player.get_state())
    board.set_last_turn_player(current_player)

    if board.has_won(current_player.get_state()):
        return 1
    elif board.has_tie():
        return 2

    return 0



