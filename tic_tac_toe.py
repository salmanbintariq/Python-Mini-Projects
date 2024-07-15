# Tic-Tac-Toe Game For Two Players

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 10)
    print()

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def check_draw(board):
    for cell in board:
        if cell not in ['X', 'O']:
            return False
    return True

# Function to get the player's move
def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                return move - 1
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to make a move
def make_move(board, move, player):
    if board[move] == ' ':
        board[move] = player
        return True
    else:
        print("This spot is already taken. Try again.")
        return False

# Main function to run the game
def tic_tac_toe():
    board = [' '] * 9
    player = 'X'

    while True:
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        move = get_move(player)
        if not make_move(board, move, player):
            continue

        if player == 'X':
            player = 'O'
        else:
            player = 'X'
tic_tac_toe()