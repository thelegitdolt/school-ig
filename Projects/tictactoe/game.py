from Projects.tictactoe.board import Board
from Projects.tictactoe.player import Player, RandomAI

def init():
    print("Welcome to TIC-TAC-TOE Game!")

    while True:
        game_mode = int(input("Please choose an opponent."
                              "\n1: Two Player"
                              "\n2: Alice, who's kind of dumb and only makes random moves"
                              "\nInput: "))

        if (not game_mode == 1) and not game_mode == 2:
            print("Invalid input! Please enter 1 or 2.")
            continue
        break

    board = Board()

    player1 = Player(input("Player 1 name: "), True)

    if game_mode == 1:
        player2 = Player(input("Player 2 name: "), False)
    else:
        player2 = RandomAI('Alice', False)


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



