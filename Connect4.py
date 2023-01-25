# Connect 4
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

clear = lambda: os.system('cls')

def draw():
    for row in board:
        print(row)

def get_input():
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
    for row in range(ROWS-1, -1, -1):
        if board[row][sel] == 0:
            board[row][sel] = current_player
            break

def check_rows(cp):
    global game_over
    count = 0
    for row in board:
        for element in row:
            if element == cp:
                count += 1
            else:
                count = 0
            if count == 4:
                game_over = True
        count = 0


while not game_over:
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    clear()
    draw()
    put_piece(get_input())
    check_rows(current_player)
clear()
draw()
print("Player {} wins!".format(current_player))



