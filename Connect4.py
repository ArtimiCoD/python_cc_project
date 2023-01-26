# Connect 4 - Importing os to clear terminal
import os

board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

ROWS = 6
COLUMNS = 7
game_over = False
current_player = 2
winner = 0

clear = lambda: os.system('cls')


def draw():
    for row in board:
        print(row)


def get_input(cp):
    print("Turn of player", cp)
    sel_col = int(input("Select column to play (0 - 6): "))
    while sel_col < 0 or sel_col > 6 or board[0][sel_col] != 0:
        clear()
        draw()
        if sel_col < 0 or sel_col > 6:
            print("Invalid input.")
        else:
            print("Column is full. try again.")
        sel_col = int(input("Select column to play (0 - 6): "))
    return sel_col


def put_piece(sel):
    global current_player
    for row in range(ROWS - 1, -1, -1):
        if board[row][sel] == 0:
            board[row][sel] = current_player
            break


def check_win(cp):
    global game_over
    count = 0
    # Checking rows
    for row in board:
        for element in row:
            if element == cp:
                count += 1
            else:
                count = 0
            if count == 4:
                game_over = True
                return cp
        count = 0
    # Checking columns
    for j in range(0, COLUMNS):
        for i in range(0, ROWS):
            if board[i][j] == cp:
                count += 1
            else:
                count = 0
            if count == 4:
                game_over = True
                return cp
        count = 0

    # Checking diagonals
    fdiaglist = [[] for _ in range(ROWS + COLUMNS - 1)]
    bdiaglist = [[] for _ in range(len(fdiaglist))]
    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            fdiaglist[j+i].append(board[i][j])
            bdiaglist[j-i+ROWS-1].append(board[i][j])

    # Creating shorter lists to count pieces
    fdiag = fdiaglist[3:9]
    bdiag = bdiaglist[3:9]

    for diag in fdiag:
        for el in diag:
            if el == cp:
                count += 1
            else:
                count = 0
            if count == 4:
                game_over = True
                return cp
        count = 0

    for diag in bdiag:
        for el in diag:
            if el == cp:
                count += 1
            else:
                count = 0
            if count == 4:
                game_over = True
                return cp
        count = 0


def check_draw():
    global game_over
    global winner
    count = 0
    upper_row = board[0]
    for el in upper_row:
        if el != 0:
            count += 1
    if count == 7:
        game_over = True
        winner = 0


# Game loop
while not game_over:

    # Player flipper
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

    clear()
    draw()
    put_piece(get_input(current_player))
    winner = check_win(current_player)
    check_draw()

clear()
draw()
if winner == 0:
    print("Draw!")
else:
    print("Player {} wins!".format(winner))
