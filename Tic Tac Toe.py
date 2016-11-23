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
