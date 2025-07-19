def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Rows, Columns and Diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def play_game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a position (1-9): ")

        if move not in "123456789":
            print("Invalid input. Try again.")
            continue

        placed = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == move:
                    board[i][j] = current_player
                    placed = True
                    break
            if placed:
                break

        if not placed:
            print("That position is already taken. Try another.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
