import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def is_winner(player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Position already taken!")
        player_move()

def computer_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"

print("Welcome to Tic Tac Toe 🎮")
print("You are X, Computer is O")

while True:
    print_board()
    player_move()

    if is_winner("X"):
        print_board()
        print("You win 🎉")
        break

    if is_draw():
        print_board()
        print("It's a draw 🤝")
        break

    computer_move()

    if is_winner("O"):
        print_board()
        print("Computer wins 😢")
        break
