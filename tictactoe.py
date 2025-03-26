from random import randrange

hor_line = "+-------+-------+-------+"
ver_lines ="|       |       |       |"
div = "  |  "
end_of_game = False
Nboard =[
        ["1","2","3"],
        ["4","X","6"],
        ["7","8","9"]
]


def display_board(board):
    print(hor_line)
    for i in range(3):
        print(ver_lines)
        print("|  ",board[i][0],div,board[i][1],div,board[i][2],"  |")
        print(ver_lines)
        print(hor_line)
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    make_list_of_free_fields(board)
    while True: # loop until player chooses free field. There is no need to check if there is an empty field because "victory_for()" already does that after each turn
        
        while True: # loop for input validation
            try:
                player_move = int(input("Enter a number from 1 to 9: " ))
            except ValueError:
                print("You entered incorrect value! Try again.")
                continue
            if player_move > 0 and player_move < 10:
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
    for row in range(3):
        for column in range(3):
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
    # I don't know how to make code for checking win conditions less bulky :c
    for i in range(3):
        if (board[0][i] + board[1][i] + board[2][i] == sign*3) or\
           (board[i][0] + board[i][1] + board[i][2] == sign*3):    # checking horisontal and vertical lines
            print(sign,"won!")
            end_of_game = True
            return
    if (board[0][0] + board[1][1] + board[2][2] == sign*3) or \
       (board[0][2] + board[1][1] + board[2][0] == sign*3):    # checking both diagonals
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
        comp_move = str(randrange(1,10))
        for item in free_fields: # checking if the field picked by randomizer is free 
            if board[item[0]][item[1]] == comp_move:
                board[item[0]][item[1]] = "X"
                make_list_of_free_fields(board)
                return
    # restart the main loop if the field is already occupied
     

            
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




