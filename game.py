import random

class Board(object):
	def __init__(self):
		self.board=[' ']*9
		self.winner=None

def printBoard(board):
	#takes a board object and prints the board in terminal
	print(' ',board.board[0], ' | ',board.board[1], ' | ',board.board[2])
	print(' ---------------')
	print(' ',board.board[3], ' | ',board.board[4], ' | ',board.board[5])
	print(' ---------------')
	print(' ',board.board[6], ' | ',board.board[7], ' | ',board.board[8])
	print('Current Winner:', board.winner)

def checkForWinner(board):
	#takes a board object and sees if anyone has one, if yes sets winner in board to that
	#Horzontals
	if(board.board[0]=='X' and board.board[1]=='X' and board.board[2]=='X'):
		board.winner='X'
	if(board.board[3]=='X' and board.board[4]=='X' and board.board[5]=='X'):
		board.winner='X'
	if(board.board[6]=='X' and board.board[7]=='X' and board.board[8]=='X'):
		board.winner='X'
	if(board.board[0]=='O' and board.board[1]=='O' and board.board[2]=='O'):
		board.winner='O'
	if(board.board[3]=='O' and board.board[4]=='O' and board.board[5]=='O'):
		board.winner='O'
	if(board.board[6]=='O' and board.board[7]=='O' and board.board[8]=='O'):
		board.winner='O'
	#Verticals
	if(board.board[0]=='X' and board.board[3]=='X' and board.board[6]=='X'):
		board.winner='X'
	if(board.board[1]=='X' and board.board[4]=='X' and board.board[7]=='X'):
		board.winner='X'
	if(board.board[2]=='X' and board.board[5]=='X' and board.board[8]=='X'):
		board.winner='X'
	if(board.board[0]=='O' and board.board[3]=='O' and board.board[6]=='O'):
		board.winner='O'
	if(board.board[1]=='O' and board.board[4]=='O' and board.board[7]=='O'):
		board.winner='O'
	if(board.board[2]=='O' and board.board[5]=='O' and board.board[8]=='O'):
		board.winner='O'
	#Diagonals
	if(board.board[0]=='X' and board.board[4]=='X' and board.board[8]=='X'):
		board.winner='X'
	if(board.board[2]=='X' and board.board[4]=='X' and board.board[6]=='X'):
		board.winner='X'
	if(board.board[0]=='O' and board.board[4]=='O' and board.board[8]=='O'):
		board.winner='O'
	if(board.board[2]=='O' and board.board[4]=='O' and board.board[6]=='O'):
		board.winner='O'

def playAction(board,move, player):
	#Takes a board and plays a move if its legal, does nothing otherwise, move is from 0-9
	# 1 2 3
	# 4 5 6
	# 7 8 9
	#Player is X or O
	if(board.board[move]==' ' and player=='X'):
		board.board[move]=player
	if(board.board[move]==' ' and player=='O'):
		board.board[move]=player
board=Board()

printBoard(board)
playAction(board,1,'X')
playAction(board,0,'X')
playAction(board,2,'X')
board.board[0]='X'
printBoard(board)
checkForWinner(board)
printBoard(board)