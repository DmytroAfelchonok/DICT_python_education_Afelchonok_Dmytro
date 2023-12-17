"""TicTacToe Project"""
import sys


def draw_field(board):
    """Function draw_field: draw_field function draw field with borders and 9 cells

       Parameters:
       str(board): board for TicTacToe game

       Returns:
       str(board): returns TicTacToe board
    """
    print("---------" + "\n" + "| " + " ".join(board[:3]) + " |"
          + "\n" + "| " + " ".join(board[3:6]) + " |"
          + "\n" + "| " + " ".join(board[6:9]) + " |" + "\n" + "---------")


def analyze_state(board):
    """Function analyze_state: This function analyzing TicTacToe game results. Win one of the side, draw or impossible.
                               if X side win, return message "X wins"
                               if 0 side win, return message "0 wins"
                               if gap "_" in board, program return an empty string, then continue
                               if no winner and if "_" not in the board, program return "Draw" message

        Parameters:
        str(board): board for TicTacToe game

        Returns:
        str x_wins: returns win for X side
        str o_wins: returns win for 0 side
        empty str: if there gap "_" in board
        str "Draw": if no winner
    """
    x_wins = o_wins = False

    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != '_':
            if board[i] == 'X':
                x_wins = True
            else:
                o_wins = True
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != '_':
            if board[i * 3] == 'X':
                x_wins = True
            else:
                o_wins = True

    if board[0] == board[4] == board[8] != '_':
        if board[0] == 'X':
            x_wins = True
        else:
            o_wins = True
    if board[2] == board[4] == board[6] != '_':
        if board[2] == 'X':
            x_wins = True
        else:
            o_wins = True

    if (x_wins and o_wins) or (board.count('X') - board.count('O')) > 1 or (board.count('O') - board.count('X')) > 1:
        print("Impossible")
        sys.exit()

    if x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' in board:
        return ""
    else:
        return "Draw"


def play_tic_tac_toe():
    """Function play_tic_tac_toe: This function create empty TicTacToe board and use draw_field and analyze_state
                                  functions.

       Parameters:
       -

       Returns:
       -
    """
    board = list("_________")
    draw_field(board)
    current_player = 'X'

    while True:
        try:
            coordinates = input("Enter the coordinates: ")
            row, col = map(int, coordinates.split())

            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Coordinates must be from 1 to 3! Try again.")
                continue

            index = (row - 1) * 3 + (col - 1)

            if board[index] == '_':
                board[index] = current_player
                draw_field(board)
                game_state = analyze_state(board)
                print(game_state)

                if game_state in ["X wins", "O wins", "Draw"]:
                    return

                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This cell is occupied! Choose another one.")

        except ValueError:
            print("You should enter numbers!")


play_tic_tac_toe()
