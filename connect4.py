import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
PIECES_TO_WIN = 4

#Method definitions part
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

#Brute force check for winning moves (maybe to change to something more optimal)
#And add possibility to change board size, number of same pieces needed to win
def winning_move(board, piece):
    #Check horizontal
    for c in range(COLUMN_COUNT-(PIECES_TO_WIN-1)):
        winning = False
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
               return True
            if board[r][c] == piece :
                for p in range(1,PIECES_TO_WIN):
                    if board[r][c+p] == piece:
                        winning = True
                    else:
                        winning = False
                #if winning :
                #    return True

    #Check vertical
    for c in range(COLUMN_COUNT):
        winning = False
        for r in range(ROW_COUNT-(PIECES_TO_WIN-1)):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
               return True
            if board[r][c] == piece:
                for p in range(1,PIECES_TO_WIN):
                    if board[r+p][c] == piece:
                        winning = True
                    else:
                        winning = False
                #if winning :
                #    return True

    #Check positive diaganols
    for c in range(COLUMN_COUNT-(PIECES_TO_WIN-1)):
        winning = False
        for r in range(ROW_COUNT-(PIECES_TO_WIN-1)):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
               return True
            if board[r][c] == piece :
                for p in range (1,PIECES_TO_WIN):
                    if board[r+p][c+p] == piece:
                            winning = True
                    else:
                        winning = False
                #if winning :
                #    return True

    #Check negative diaganols
    for c in range(COLUMN_COUNT-(PIECES_TO_WIN-1)):
        for r in range(PIECES_TO_WIN-1, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
               return True

#Core program
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

            if winning_move(board,1) :
                print("Player 1 wins.")
                game_over = True

    #Ask player 2 for input
    else:
        column = int(input("Player 2 make your selection (0-6):"))
    
        if is_valid_location(board, column) :
            row = get_next_open_row(board,column)
            drop_piece(board,row,column,2)

            if winning_move(board,2) :
                print("Player 2 wins.")
                game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2


