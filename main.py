import random

ALL_SPACES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X, O, BLANK = "X", "O", " "


def get_blank_board():
    board = {}  # Board is blank
    for space in ALL_SPACES:  # For number inside ALL_SPACES
        board[space] = BLANK  # Change that space to make it BLANK
    return board  # Return the board


def display_board(board):  # Nothing much just board layout
    print(f"""
    {board[1]}|{board[2]}|{board[3]}    1 2 3 
    -+-+-
    {board[4]}|{board[5]}|{board[6]}    4 5 6
    -+-+-
    {board[7]}|{board[8]}|{board[9]}    7 8 9
""")


def is_valid_space(board, move):
    if move in ALL_SPACES and board[move] == BLANK:
        return True
    else:
        return False


def main():
    board = get_blank_board()
    print("Do you want to play as X or O?")
    letter = input("> ").upper()
    if letter == X:
        player_symbol, computer_symbol = X, O
        turn = "player"
    else:
        player_symbol, computer_symbol = O, X
        turn = "computer"

    display_board(board)
    while True:
        if turn == "player":
            move = get_move(player_symbol, board)
            update_board(board, player_symbol, move)
            if is_winner(player_symbol, board):
                print(f"{player_symbol} has won!")
                break
            elif the_full_board_2(board):
                display_board(board)
                print("It's a Tie")
                break
            else:
                display_board(board)
                turn = "computer"
        else:
            move = get_computer_move(computer_symbol, board)
            update_board(board, computer_symbol, move)
            if is_winner(computer_symbol, board):
                display_board(board)
                print(f"{computer_symbol} has won!")
                break
            elif the_full_board_2(board):
                display_board(board)
                print("It's a Tie")
                break
            else:
                display_board(board)
                turn = "player"


def get_computer_move(computer_symbol, board):
    if computer_symbol == "X":
        player_symbol = "O"
    else:
        player_symbol = "X"
    # try to take centre

    # Check if bot can win in the next move
    for move in board.keys():
        board_copy = board.copy()
        if is_valid_space(board_copy, move):
            update_board(board_copy, computer_symbol, move)
            if is_winner(computer_symbol, board_copy):
                return move

    for move in board.keys():
        board_copy = board.copy()
        if is_valid_space(board_copy, move):
            update_board(board_copy, player_symbol, move)
            if is_winner(player_symbol, board_copy):
                return move

    if is_valid_space(board, 5):
        return 5

    # Try to take corner, if it is free. [1, 3, 5, 7]
    possible_moves = []
    for move in [1, 3, 5, 7]:
        if is_valid_space(board, move):
            possible_moves.append(move)
        if len(possible_moves) != 0:
            return random.choice(possible_moves)

    # Try to take the cross if possible
    possible_moves = []
    for move in [2, 4, 6, 8]:
        if is_valid_space(board, move):
            possible_moves.append(move)
        if len(possible_moves) != 0:
            return random.choice(possible_moves)


def swap_turn(currentplayer, next_player):
    currentplayer, next_player = next_player, currentplayer
    return currentplayer


def get_move(player, board):
    print(f"What will {player} do? [1 - 9| Numbers represent the spaces]")
    move = None
    while not is_valid_space(board, move):
        move = int(input("> "))
        if not is_valid_space(board, move):
            print("Bro, that gap is full!")
    return move


def update_board(board, currentplayer, move):
    board[move] = currentplayer


def is_winner(player, board):
    if board[1] == board[2] == board[3] == player:  # Top
        return True
    elif board[4] == board[5] == board[6] == player:  # Mid
        return True
    elif board[7] == board[8] == board[9] == player:  # Bottom
        return True

    elif board[1] == board[4] == board[7] == player:  # left
        return True
    elif board[2] == board[5] == board[8] == player:  # Mid
        return True
    elif board[3] == board[6] == board[9] == player:  # left
        return True

    elif board[1] == board[5] == board[9] == player:  # left
        return True
    elif board[3] == board[5] == board[7] == player:  # left
        return True

    else:
        return False


def the_full_board(board):
    for space in board:
        if board[space] == BLANK:
            return False
    return True


def the_full_board_2(board):
    blank_space = list(board.values())
    if blank_space.count(BLANK) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
