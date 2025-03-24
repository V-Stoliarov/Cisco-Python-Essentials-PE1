from random import randrange

hor_line = "+-------+-------+-------+"
ver_lines ="|       |       |       |"
div = "  |  "
end_of_game = True
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
    field_is_free = True
    while field_is_free:
        field_is_free = True
        player_move = int(input("Enter a number from 1 to 9:" ))
        if 1 < player_move or player_move > 9:
            print()
            continue
        else:
            for item in free_fields:
                if board[item[0]][item[1]] == player_move:
                    board[item[0]][item[1]] = "O"
                    field_is_free = False
                    make_list_of_free_fields(board)
                    break
            else:
                print("The field",player_move,"is already occupied!")
                continue
    victory_for(board,"O")
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
    make_list_of_free_fields(Nboard)
    # temporary bruteforce approach for win condition
    if (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
         (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
         (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or \
         (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
         (board[0][2] == sign and board[1][1] == sign and board[2][2] == sign):
        print(sign,"won")
        end_of_game = False
        return
    elif len(free_fields) == 0:
        print("No one won")
        end_of_game = False
        return
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    make_list_of_free_fields(Nboard)
    field_is_free = True
    while field_is_free:
        field_is_free = True
        comp_move = str(randrange(1,10))
        for item in free_fields:
            if board[item[0]][item[1]] == comp_move:
                board[item[0]][item[1]] = "X"
                field_is_free = False
                make_list_of_free_fields(Nboard)
                break
    victory_for(board,"X") 

            

            
while end_of_game:
    make_list_of_free_fields(Nboard)
    enter_move(Nboard)
    display_board(Nboard)
    draw_move(Nboard)
    display_board(Nboard)



