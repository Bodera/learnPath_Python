#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

#range(5) es un acceso directo para range(0, 5)
board = [] #crea una cuadrícula de 5x5 con todos los "O"s, para "océano".

for O in range(5): #horizontal 
	board.append(5 * ["O"]) #vertical
	#board.append(5 * " O  ")

for value in board: 
	print(value) #proba

#print(board)
print_board(board_in):
	for value in board:
		print(value)