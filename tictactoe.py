import random
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*5)

def check_win(board,player):
    
    for row in board:
        if all(s==player for s in row):
            return True
        
    for col in range(3):
        if all(board[row][col]==player for row in range(3)):
            return True
        
    if all(board[i][i]==player for i in range(3)):
        return True
    if all(board[i][2-i]==player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell in["X","O"] for row in board for cell in row)

def computer_move(board):
    empty=get_empty_cell(board)
    return random.choice(empty)
def get_empty_cell(board):
    return [(r,c) for r in range(3) for c in range(3) if board[r][c]==" "]


def tictactoe():
    board=[[" " for i in range(3)]for j in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("Let's play with computer")
    print("You are 'X',Computer is 'O'")
    print_board(board)

    while True:
        try:
            # Player's Move
            row=int(input("Enter row (0-2): "))
            col=int(input("Enter col (0-2): "))
            if board[row][col]!=" ":
                print("That cell is already filled ")
                print("Choose another one")
                continue
            board[row][col]="X"
        except :
            print("Invalid input! choose 0,1,or 2")
            continue
        print("Board after Player's choice")
        print_board(board)

        if check_win(board,"X"):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a Draw!")
            print("Try again to win!")
            break
        #Computer's Move
        r,c=computer_move(board)
        board[r][c]="O"
        print("Board after Computer's choice")
        print_board(board)

        if check_win(board,"O"):
            print("Better Luck next time! Computer wins!")
            break
        if check_draw(board):
            print("It's a Draw!")
            print("Try again to win!")
            break


tictactoe()