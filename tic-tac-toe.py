EMPTY = ' '
board = [EMPTY] * 9


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

HUMAN = 'X'
Tic_Tac_AI = 'O'
def is_game_over():
    return any(winning_combination(player) for player in [HUMAN, Tic_Tac_AI]) or EMPTY not in board

def winning_combination(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def human_move():
    while True:
        try:
            move = int(input("Press (1-9) for your move: ")) - 1
            if move >= 0 and move < 9 and board[move] == EMPTY:
                board[move] = HUMAN
                break
            else:
                print("Invalid move :( ")
        except ValueError:
            print("Invalid input. Enter a number (1-9).")

def Tic_Tac_AI_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = Tic_Tac_AI
            score = minimax(board, 0, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = Tic_Tac_AI

# Minimax algorithm without Alpha-Beta Pruning
def minimax(board, depth, is_maximizing):
    if winning_combination(HUMAN):
        return -1
    elif winning_combination(Tic_Tac_AI):
        return 1
    elif is_game_over():
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = Tic_Tac_AI
                eval = minimax(board, depth + 1, False)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
        return min_eval

# MTic_Tac_AIn game loop
while True:
    print_board()
    if is_game_over():
        if winning_combination(HUMAN):
            print("You win!")
        elif winning_combination(Tic_Tac_AI):
            print("Tic_Tac_AI wins!")
        else:
            print("It's a draw!")
        break

    if any(cell == EMPTY for cell in board):
        human_move()
        print_board()
    else:
        print("It's a draw!")
        break

    if is_game_over():
        if winning_combination(HUMAN):
            print("You win!")
        elif winning_combination(Tic_Tac_AI):
            print("Tic_Tac_AI wins!")
        else:
            print("It's a draw!")
        break

    if any(cell == EMPTY for cell in board):
        Tic_Tac_AI_move()
    else:
        print("It's a draw!")
        break
