#Tic Tac Toe game
import random

def drawBoard(board):
	print("	|	|")
	print("" + board[7] + "|" + board[8] + "|" + board[9])
	print("	|	|")
	print("--------------")	
	print("	|	|")
	print("" + board[4] + "|" + board[5] + "|" + board[6])
	print("	|	|")
	print("--------------")	
	print("	|	|")
	print("" + board[1] + "|" + board[2] + "|" + board[3])
	print("	|	|")

# draw = [' ', ' ', ' ', ' ', 'X', 'O', ' ', 'X', ' ', 'O'];
# drawBoard(draw);