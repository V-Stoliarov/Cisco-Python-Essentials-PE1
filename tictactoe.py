from random import randrange

hor_line = "+---------"
ver_lines ="|         "
end_of_game = False


def generate_board():
    global n
    global Nboard
    while True: # loop for input validation
        try:
            n = int(input("Enter an odd number equal to or higher than 3 to set board size: " ))
        except ValueError:
            print("You entered incorrect value! Try again.")
            continue
        if n > 2 and n % 2 == 1:
            break
    Nboard = [[0 for j in range(n)] for i in range(n)]    
    count = 1
    for i in range(n):
        for j in range(n):
           Nboard[i][j] = str(count)
           count += 1
    Nboard[n//2][n//2] = "X"

    

def display_board(board):
    print(hor_line*n+"+")
    for i in range(n):
        print(ver_lines*n+"|")
        stor =""
        for j in range(n-1):
            stor += f'{board[i][j]:{" "}^{9}}' + "|" 
        print("|" + stor + f'{board[i][n-1]:{" "}^{9}}'+"|")
        print(ver_lines*n+"|")
        print(hor_line*n+"+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    make_list_of_free_fields(board)
    while True: # loop until player chooses free field. There is no need to check if there is an empty field because "victory_for()" already does that after each turn
        
        while True: # loop for input validation
            try:
                print(f"Enter a number from 1 to {n**2}: ") 
                player_move = int(input())
            except ValueError:
                print("You entered incorrect value! Try again.")
                continue
            if player_move > 0 and player_move < n**2+1:
                break
                
        for item in free_fields: # check if the field entered by player is free
            if board[item[0]][item[1]] == str(player_move):
                board[item[0]][item[1]] = "O"
                make_list_of_free_fields(board)
                return # free field was found and assigned, exit the function
        else:
            print("The field",player_move,"is already occupied!") 
            # restart the entire loop
        
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    global free_fields
    free_fields = []
    for row in range(n):
        for column in range(n):
            if board[row][column] == "X" or board[row][column] == "O" :
                continue
            else:
                free_fields.append((row,column))

    return free_fields
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.



def victory_for(board, sign):
    global end_of_game
    make_list_of_free_fields(board)
    board_tr = [list(row) for row in zip(*board)]
    diag_1 = ''
    diag_2 = ''
    
    for i in range(n):
        diag_1 += board[i][i]
        diag_2 += board[i][n-1-i]
        hori = ''.join(board[i])
        vert = ''.join(board_tr[i])
        if (hori == sign*n) or (vert == sign*n):    # checking horisontal and vertical lines
            print(sign,"won!")
            end_of_game = True
            return
    
    if (diag_1 == sign*n) or (diag_2 == sign*n):    # checking both diagonals
        print(sign,"won!")
        end_of_game = True
        return
    if len(free_fields) == 0:
        print("No one won.")
        end_of_game = True
        return
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    make_list_of_free_fields(board)
    while True: # loop until randomizer chooses a free field
        comp_move = str(randrange(1,n**2+1))
        for item in free_fields: # checking if the field picked by randomizer is free 
            if board[item[0]][item[1]] == comp_move:
                board[item[0]][item[1]] = "X"
                make_list_of_free_fields(board)
                return
    # restart the main loop if the field is already occupied
     


generate_board()              
display_board(Nboard)            
while end_of_game == False: 
    enter_move(Nboard)
    display_board(Nboard)
    victory_for(Nboard,"O")
    if end_of_game == True:
        break
    print("The move of X:")
    draw_move(Nboard)
    display_board(Nboard)
    victory_for(Nboard,"X")





