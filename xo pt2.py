ALL_SPACES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X, O, BLANK = "X", "O", " "


def get_blank_board():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def display_board(board):
    print(f"""
    {board[1]}|{board[2]}|{board[3]}   1 2 3
    -+-+-
    {board[4]}|{board[5]}|{board[6]}   4 5 6
    -+-+-
    {board[7]}|{board[8]}|{board[9]}   7 8 9
""")


def is_valid_space(board, move):
    if move in ALL_SPACES and board[move] == BLANK:
        return True
    else:
        return False


def main():
    board = get_blank_board()
    current_player, next_player = X, O
    while True:
        display_board(board)

        move = get_move(current_player, board)

        update_board(board, current_player, move)

        winner = is_winner(current_player, board)
        if winner:
            display_board(board)
            print(f"{current_player} is winner!")
            break
        full_board = is_full_board_2(board)
        if full_board:
            display_board(board)
            print("The game is a tie!")
            break

        current_player, next_player = next_player, current_player


def get_move(player, board):
    print(f"What is {player}'s move? (1-9)")
    move = None
    while not is_valid_space(board, move):
        move = int(input("> "))
        if not is_valid_space(board, move):
            print('Please enter another block')
    return move


def update_board(board, current_player, move):
    board[move] = current_player


def is_winner(player, board):
    if board[1] == board[2] == board[3] == player:  # Across Top
        return True
    elif board[4] == board[5] == board[6] == player:  # Across Middle
        return True
    elif board[7] == board[8] == board[9] == player:  # Across Bottom
        return True

    elif board[1] == board[4] == board[7] == player:  # Left
        return True
    elif board[2] == board[5] == board[8] == player:  # Middle
        return True
    elif board[3] == board[6] == board[9] == player:  # Right
        return True

    elif board[1] == board[5] == board[9] == player:  # Diagonal Left
        return True
    elif board[3] == board[5] == board[7] == player:  # Diagonal Right
        return True

    else:
        return False


def is_full_board_1(board):
    for space in board:
        if board[space] == BLANK:
            return False
    return True


def is_full_board_2(board):
    blank_space = list(board.values())
    if blank_space.count(BLANK) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

# Data Structure:
# - List -> []
# - Dictionary -> {}
# - Set -> {}
# - Tuple -> ()
