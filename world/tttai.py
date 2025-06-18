import random as r

def init_board():
    return [' '] * 9

def display_board(board):
    print()
    for i in range(3):
        row = []
        for j in range(3):
            idx = i * 3 + j
            cell = board[idx] if board[idx] != ' ' else str(idx)
            row.append(cell)
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()

def get_available_moves(board):
    return [i for i, val in enumerate(board) if val == ' ']

def make_move(board, player, move):
    if board[move] != ' ':
        raise ValueError("Invalid move: spot already taken.")
    new_board = board.copy()
    new_board[move] = player
    return new_board

def check_game_status(board):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] != ' ':
            return f"{board[a]} wins"
    if ' ' not in board:
        return "Draw"
    return "Ongoing"

def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                return move
            else:
                print("Spot taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 0 to 8.")
#def aimove(board,options = [0,1,2,3,4,5,6,7,8]):
    #while True:
        #move = r.choice(options)
        #if board[move] == ' ':
            #return move
        #else:
            #options.remove(move)
            #aimove(board,options)
                    
def aimove_random(board):
    options = get_available_moves(board)
    return r.choice(options)

def minimax(board, current_player):
    status = check_game_status(board)
    if status != "Ongoing":
        if status == f"{current_player} wins":
            return 1
        elif status == "Draw":
            return 0
        else:
            return -1
    next_player = 'O' if current_player == 'X' else 'X'
    scores = []

    for move in get_available_moves(board):
        new_board = make_move(board, current_player, move)
        score = -minimax(new_board, next_player)  # Negamax: flip sign for opponent
        scores.append(score)

    return max(scores)

def aimove_dfs(board, player):
    best_score = -float('inf')
    best_move = None

    for move in get_available_moves(board):
        print(best_score,board)
        new_board = make_move(board, player, move)
        score = -minimax(new_board, 'O' if player == 'X' else 'X')
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def play_game():
    board = init_board()
    current_player = 'X'
    while True:
        if current_player == "X":
            display_board(board)
            print(f"{current_player}'s turn")
            move = get_human_move(board)
            board = make_move(board, current_player, move)
            status = check_game_status(board)
            if status != "Ongoing":
                display_board(board)
                print(status)
                break
        elif current_player == "O":
            display_board(board)
            print(f"{current_player}'s turn")
            move = aimove_dfs(board,current_player)
            board = make_move(board, current_player, move)
            status = check_game_status(board)
            if status != "Ongoing":
                display_board(board)
                print(status)
                break
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game loop
play_game()
