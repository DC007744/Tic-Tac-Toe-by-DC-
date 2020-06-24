#VARIABLES
board = ["_" , "_", "_", 
         "_" , "_", "_",
         "_" , "_", "_"]

current_player = 'X'
game_still_going = True
position = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#FUNCTIONS
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    if board[position] == "_":
        board[position] = player
        display_board()

    else:
        print("You cannot choose to play there. Go  again!")
        handle_turn(player)


def flip_turn():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

    return current_player


def check_for_win():
    check_rows()
    check_columns()
    check_diagonals()


                                                        # WINNER FUNCTION
def check_rows():
    global game_still_going

    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"

    if row1 or row2 or row3:
        game_still_going = False

    return game_still_going


def check_columns():
    global game_still_going

    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"

    if column1 or column2 or column3:
        game_still_going = False

    return game_still_going


def check_diagonals():
    global game_still_going

    diagonal1 = board[0] == board[4] == board[8] != "_"
    diagonal2 = board[6] == board[4] == board[2] != "_"

    if diagonal1 or diagonal2:
        game_still_going = False

    return game_still_going

                                                        # WINNER FUNCTION
def check_for_tie():
    global game_still_going

    if "_" not in board:
        game_still_going = False
        return True
    else:
        return False

def check_for_win_or_tie():
    check_for_win()
    check_for_tie()

# ----MAIN FUNCTION----
def play_game():
    global game_still_going

    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_for_win_or_tie()
        flip_turn()
    else:
        flip_turn()
        print(current_player + " wins!")


play_game()