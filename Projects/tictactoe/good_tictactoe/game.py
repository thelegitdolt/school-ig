from Projects.tictactoe.good_tictactoe.board import Board
from Projects.tictactoe.good_tictactoe.player import Player, AI, MinimaxAI


def init():
    print("Welcome to TIC-TAC-TOE Game!")

    while True:
        game_mode = input("Please choose an opponent."
                          "\n1: Two Player"
                          "\n2: Alice, who's kind of dumb and only makes random moves"
                          "\n3: Bob, A tic tac toe mastermind who calculates every move"
                          "\nInput: ")

        if not game_mode.isnumeric() or not 0 < (game_mode := int(game_mode)) < 4:
            print("Invalid input! Please enter 1, 2, or 3.")
            continue
        break


    player1 = Player(input("Player 1 name: "), True)

    if game_mode == 1:
        player2 = Player(input("Player 2 name: "), False)
    elif game_mode == 2:
        player2 = AI('Alice', False)
    else:
        player2 = MinimaxAI('Bob', False)

    board = Board()

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

    coordinate = current_player.choose(board)

    board.set_board(coordinate, current_player.get_state())
    board.set_last_turn_player(current_player)

    result = board.get_result()
    if result.isupper():
        return 1
    elif result == 't':
        return 2

    return 0
