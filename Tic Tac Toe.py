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

def inputPlayerLetter():
	letter = ""
	while not (letter=='X' or letter == 'O'):
		print("Do you want to be X or O?")
		letter = raw_input.upper()
	if letter == 'X':
		return ['X','O']
	else:
		return['O','X']

def whoGoesFirst():
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
		
#function returns True if the player types in 'yes', 'YES', 'y', or anything that begins with the letter Y
def playAgain():
	print("Do you want to play again? (yes or no) ")
	return input().lower().startswith('y')	

def makeMove(board,letter,move):
	board[move] = letter

def isWinner(board, letter):
	return ((board[7] == letter and board[8] == letter and board[9] == letter) or
			(board[6] == letter and board[5] == letter and board[4] == letter) or
			(board[1] == letter and board[2] == letter and board[3] == letter) or
			(board[1] == letter and board[4] == letter and board[7] == letter) or
			(board[2] == letter and board[5] == letter and board[8] == letter) or 
			(board[3] == letter and board[6] == letter and board[9] == letter) or 
			(board[1] == letter and board[5] == letter and board[9] == letter) or
			(board[3] == letter and board[5] == letter and board[7] == letter))

def getBoardCopy(board):
	dupeBoard = []
	for i in board:
		dupeBoard.append(i)
	return dupeBoard

def isSpaceFree(board, move):
	return board[move] == ''

