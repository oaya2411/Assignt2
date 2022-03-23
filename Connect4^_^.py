#FCAI.CU,Programming 1 – 2022 - Assignment 2
#Program Name: connect4.pyhton.
#Program Description: game in python language.
#Last Modification Date: 23/3/2022
#Author and ID and Group: Aya Osama Mohammed.
#Teaching Assistant: DR.Mohammed EL-ramly.
#Purpose:help another one who doesn't know as i was ,too.

import numpy as np  #it's a library to create the board of the game as simple game without gui.

def display_screen():
    board=np.zeros((6,7))
    return board
board = display_screen()
print(board)
# we create an board with 6 rows and 7 colums with the function display_board and show it on the consol application

def valid_location(board,col):
    return board[5][col]==0

#we need to make sure that the place that user will choose to play is valid so we create the above function for that.

def open_index(board,col):

    for row in range(6):
        if board[row][col]==0:
            return row

#the valid index on our board is the place that is carrying the 0 value.
#we need a function of open_index to replace the 0 with the new value of each player.

def print_screen(board):
    board=np.flip(board,0)
    print(board)

#we need to make flip to the board to make dealing with it easy.
#After replace it we need to show it Again by the following function.

def update_board(board, col, row, piece):
    board[row][col]=piece

def is_winner(player,col): #this function check the winner player with it's cases"vertically-horizontally-diagonal right or left"
    for c in range(6):
        for r in range(4):
            if board[c][r]==board[c][r+1]==board[c][r+2]==board[c][r+3] and board[c][r]!=0:
                return True
    for r in range(7):
        for c in range(3):
            if board[c][r]==board[c+1][r]==board[c+2][r]==board[c+3][r] and board[c][r]!=0:
                return True
    for c in range(3):
        for r in range(4):
            if board[c][r]==board[c+1][r+1]==board[c+2][r+2]==board[c+3][r+3] and board[c][r]!=0:
                return True
    for c in range(3):
        for r in range(3,7):
            if board[c][r]==board[c+1][r-1]==board[c+2][r-2]==board[c+3][r-3] and board[c][r]!=0:
                return True


game_over = False # it's meaning that the pklay is still true and there isn't lose.
turn =0 # we suppose that the initial turn for each player is zero.
n_actions=0 # this game with 42 actions by the way 42 indexes so we suppose that n_actions=0.
 # the start of the game so syer that isn't game over.
while n_actions<=42:
    if turn==0:
        n_actions += 1
        col= int(input("Player one please enter your colum (0,6): "))# to take the number of the index you want to create
        if col<7:
                turn += 1
                turn=turn%2 #we make adivision by two to turn between the two player so turn if of player one always=0 and player2 always =1.
                if valid_location(board, col):
                    row = open_index(board, col)
                    update_board(board, col, row, 1)
                    print_screen(board)
                    if is_winner(1,col):
                        print("player 1 is win ^_^")
                        break



    elif turn!=0:
        n_actions += 1
        col = int(input("Player 2 please enter your colum (0,6): "))
        turn +=1
        turn=turn%2
        if valid_location(board, col):
            row = open_index(board, col)
            update_board(board, col, row, 2)
            print_screen(board)
            if is_winner(2, col):
                print("player 2 is win^_^")
                break
    else:
        print("Drew!")


#As soon as one of hte player win the loop will break and we will have a winner else they will be equal to each other.





