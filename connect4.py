import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

#Initialize board as numpy array
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

#Drop a piece at given row and column
def drop_piece(board, row, column, piece):
    board[row][column] = piece

#Loop through a given column to check if there is any empty slot
def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0

#Return first empty row slot
def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

#numpy 2D array are built top-down
def print_board(board):
    print(np.flip(board,0))

board = create_board()
game_over = False
turn = 0
print_board(board)

while not game_over:
    #Ask player 1 for input
    if turn == 0:
        column = int(input("Player 1 make your selection (0-6):"))

        if is_valid_location(board, column) :
            row = get_next_open_row(board,column)
            drop_piece(board,row,column,1)

    #Ask player 2 for input
    else:
        column = int(input("Player 2 make your selection (0-6):"))
    
        if is_valid_location(board, column) :
            row = get_next_open_row(board,column)
            drop_piece(board,row,column,2)

    print_board(board)

    turn += 1
    turn = turn % 2


