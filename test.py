
winx = False
wino = False
move = int(0)
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def determine():
    win()
    if winx:
        print("X wins")
        return True
    elif wino:
        print("O wins")
        return True
    return False

def board_display():
    print("---------")
    print("|", board[0][0],  board[0][1], board[0][2], "|")
    print("|", board[1][0],  board[1][1], board[1][2], "|")
    print("|", board[2][0],  board[2][1], board[2][2], "|")
    print("---------")

board_display()

def win():
    global winx
    global wino
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            winx = True
        elif board[0][0] == 'O':
            wino = True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            winx = True
        elif board[0][2] == 'O':
            wino = True
    else:
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    winx = True
                elif board[i][0] == 'O':
                    wino = True
        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    winx = True
                elif board[0][i] == 'O':
                    wino = True

board2 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
flag = True
emptycount = 9
while True:
    moves = input("Enter the coordinates:")
    coords = moves.split(" ")
    if coords[0].isalpha() or coords[1].isalpha():
        print("You should enter numbers!")
    elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        if int(coords[0]) == 1 and int(coords[1]) == 1:
            if board[2][0] == "X" or board[2][0] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            elif move % 2 == 0:
                board[2][0] = "X"
            else:
                board[2][0] = "O"
        elif int(coords[0]) == 1 and int(coords[1]) == 2:
            if board[1][0] == "X" or board[1][0] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[1][0] = "X"
            else:
                board[1][0] = "O"
        elif int(coords[0]) == 1 and int(coords[1]) == 3:
            # board[0][0] = "X"
            if board[0][0] == "X" or board[0][0] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[0][0] = "X"
            else:
                board[0][0] = "O"
        elif int(coords[0]) == 2 and int(coords[1]) == 1:
            #board[2][1] = "X"
            if move % 2 == 0:
                board[2][1] = "X"
            else:
                board[2][1] = "O"
        elif int(coords[0]) == 2 and int(coords[1]) == 2:
            #board[1][1] = "X"
            if board[1][1] == "X" or board[1][1] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[1][1] = "X"
            else:
                board[1][1] = "O"
        elif int(coords[0]) == 2 and int(coords[1]) == 3:
            #board[0][1] = "X"
            if board[0][1] == "X" or board[0][1] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[0][1] = "X"
            else:
                board[0][1] = "O"
        elif int(coords[0]) == 3 and int(coords[1]) == 1:
            #board[2][2] = "X"
            if board[2][2] == "X" or board[2][2] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[2][2] = "X"
            else:
                board[2][2] = "O"
        elif int(coords[0]) == 3 and int(coords[1]) == 2:
            #board[1][2] = "X"
            if board[1][2] == "X" or board[1][2] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[1][2] = "X"
            else:
                board[1][2] = "O"
        elif int(coords[0]) == 3 and int(coords[1]) == 3:
            #board[0][2] = "X"
            if board[0][2] == "X" or board[0][2] == "O":
                flag = False
                print("This cell is occupied! Choose another one!")
            if move % 2 == 0:
                board[0][2] = "X"
            else:
                board[0][2] = "O"
        if flag:
            move += 1
            emptycount -= 1
            board_display()
            if determine():
                break
            if emptycount == 0:
                print("Draw")
                break
        flag=True
