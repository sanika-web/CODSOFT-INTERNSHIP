
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")

def check_winner(board, player):
    win = [(0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8),
           (0,4,8), (2,4,6)]
    return any(board[x] == board[y] == board[z] == player for x,y,z in win)

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, is_ai):
    if check_winner(board, 'O'): return 1
    if check_winner(board, 'X'): return -1
    if ' ' not in board: return 0

    if is_ai:
        best = -float('inf')
        for i in available_moves(board):
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            best = max(score, best)
        return best
    else:
        best = float('inf')
        for i in available_moves(board):
            board[i] = 'X'
            score = minimax(board, True)
            board[i] = ' '
            best = min(score, best)
        return best

def ai_move(board):
    best_score = -float('inf')
    move = None
    for i in available_moves(board):
        board[i] = 'O'
        score = minimax(board, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    print_board(board)

    while True:
    
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Cell taken! Try again.")
                continue
            board[move] = 'X'
        except:
            print("Invalid input.")
            continue

        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

        print("AI's turn.")
        ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

play_game()