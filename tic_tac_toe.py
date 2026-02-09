from random import randrange

for i in range(10):
    print(randrange(8))
    
    
def display_board(board):
    board = [[i+3*j for i in range(1,4)] for j in range(3)]
    return board

new_board=[]
result=display_board(new_board)
print(result)

# Function to display the board
def display_board(board):
    print("=" * 19)
    for row in board:
        print("|  " + "  |  ".join(row) + "  |")
        print("=" * 19)

#Function to enter the players move        
def enter_move(board):
    while True:
        move = input('Enter your move(1-9):')
        
        if move.isdigit() and 1 <= int(move) <= 9:
            move=int(move)
            i=(move-1)//3
            j=(move-1)%3
            if board[i][j].isdigit():
                board[i][j]='X'
                break
            else:
                print('Cell has been taken. Enter a different move (1-9):')
        else:
            print('Invalid input. Enter a number between 1 and 9:')
    
#list of free fields    
def make_list_of_free_fields(board):
    free_fields=[]
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                free_fields.append((i,j))
    return free_fields

#check who won
def victory_for (board, sign):
    #check rows
    for row in board:
        if all(cell == sign for cell in row):
            print("Player using", sign, "won")
            return True
    #check columns
    for col in range(3):
        if all(board[row][col]==sign for row in range(3)):
            print('Player using', sign, 'won')
            return True
    #check diagonals
    if all(board[i][i]==sign for i in range(3)):
        print('Player using', sign, 'won')
        return True
    if all(board[i][2-i]==sign for i in range(3)):
        print('Player using', sign, 'won')
        return True
    
    #check if there is a winner
    print('No winner yet')
    return False

#draw the computer's move
def draw_move(board):
    move = randrange(1, 10)  # random number 1–9
    # Keep generating until we find a free cell
    while not any(move == int(cell) for row in board for cell in row if cell.isdigit()):
        move = randrange(1, 10)
    
    # Replace the chosen number with "O"
    for i in range(3):
        for j in range(3):
            if board[i][j] == str(move):
                board[i][j] = "O"
                return  # stop after placing

# Example usage
board = [[str(i + j*3) for i in range(1,4)] for j in range(3)]
display_board(board)

free_fields = make_list_of_free_fields(board)
print("Free fields:", free_fields)

draw_move(board)
print("\nAfter computer move:\n")
display_board(board)

enter_move(board)

victory_for(board,'X')