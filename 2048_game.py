# -*- coding: utf-8 -*-
"""2048_Game"""

import random
import copy



#Merging Tiles in Left Direction
def merge_row_left(row):
  #check if left tile is empty
  for x in range(board_size-1):
    for i in range(board_size-1, 0, -1):
      #if empty, move current tile to left
      if row[i-1] == 0:
        row[i-1] = row[i]
        row[i] = 0

  for i in range(board_size-1):
    #If tiles are equal, double current tile
    if row[i] == row[i+1]:
      row[i] *= 2
      row[i+1] = 0  #make right tile empty/0

  for i in range(board_size-1, 0, -1):
    #if left tile is empty, move current tile to left
    if row[i-1] == 0:
      row[i-1] = row[i]
      row[i] = 0

  return row



#Transpose for Vertical Movement
def transpose(game_board):
  for i in range(board_size):
    for j in range(i, board_size):
      #If current row number and column number are not same
      #Take Transpose for vertical movement
      if not i==j:
        _temp = game_board[i][j]
        game_board[i][j] = game_board[j][i]
        game_board[j][i] = _temp
  return game_board



#Reverse Row for Right Movement
def reverse(row):
  _temp_row = []
  for i in range (board_size - 1, -1, -1):
    _temp_row.append(row[i])
  return _temp_row



#Merging Rows in Left Direction
def merge_left(game_board):
  for i in range(board_size):
    #Sending Row to merge in left direction
    game_board[i] = merge_row_left(game_board[i])
  return game_board



#Merging Rows in Right Direction
def merge_right(game_board):
  for i in range(board_size):
    #Sending Row to reverse it
    game_board[i] = reverse(game_board[i])
    #Sending Row to merge in right direction
    game_board[i] = merge_row_left(game_board[i])
    #Sending Row to Re-reverse it
    game_board[i] = reverse(game_board[i])
  return game_board



#Merging Rows in Up Direction
def merge_up(game_board):
  game_board = transpose(game_board)  #Transpose
  game_board = merge_left(game_board) #Merging left
  #Transpose(Now merging will be seen in upward direction)
  game_board = transpose(game_board)
  return game_board



#Merging Rows in Down Direction
def merge_down(game_board):
  game_board = transpose(game_board) #Transpose
  game_board = merge_right(game_board) #Merging Right
  #Transpose(Now merging will be seen in downward direction)
  game_board = transpose(game_board)
  return game_board



#Finding Largest Number in Board for tile spaces/size
def find_lagest_num():
  largest_num = 0
  for row in board:
    for element in row:
      if largest_num < element:
        largest_num = element
  return str(largest_num)



#Display Game Board
def display():
  #Finding Largest number in board
  num_spaces = len(find_lagest_num())
  for row in board:
    row_str = "|"
    for element in row:
      if element == 0:
        row_str += " " * num_spaces + "|"
      else:
        row_str += (" " * (num_spaces - len(str(element)))) + str(element) + "|"

    print(row_str)



#Picking random tile on board
#for placing new num (2 or 4)
def place_num():
  while(True):
    #picking random row and column
    rand_row = random.randint(0, board_size - 1)
    rand_col = random.randint(0, board_size - 1)

    #If the tile is empty
    if board[rand_row][rand_col] == 0:
      #Calling Function to place random num on board
      board[rand_row][rand_col] = random_num()
      return



#Checks if 2048 present in board
def win_check():
  for row in board:
    if 2048 in row:
      display()
      print("Congrats you won!")
      return True
  return False



#Check if no movement possible
def no_moves():
  _temp1 = copy.deepcopy(board)
  _temp1 = merge_down(_temp1)
  if _temp1 == board:
    _temp1 = merge_up(_temp1)
    if _temp1 == board:
      _temp1 = merge_left(_temp1)
      if _temp1 == board:
        _temp1 = merge_right(_temp1)
        if _temp1 == board:
          print("You Lost")
          return True
  return False



#Random value generation, 2 or 4
def random_num():
  return random.choice([2,4])



#Creating Board
def create_board():
  board = []
  for i in range(board_size):
    row = []
    for j in range(board_size):
      row.append(0)
    board.append(row)

  #Random Generating value at 2 spots
  #at starting of game
  _count = 0  #count for spots filled
  while(_count<2):
    #picking random row and column
    rand_row = random.randint(0, board_size - 1)
    rand_col = random.randint(0, board_size - 1)

    if board[rand_row][rand_col] == 0:
      board[rand_row][rand_col] = random_num()
      _count += 1

  return board





board_size = 4 #Default board size = 4, changeable
game_over = False #Ceck if player won or lost
board = create_board()
display()

while not game_over:
  _temp_board = copy.deepcopy(board)  #temporary board, to check if movement possible
  movement = input("Enter wasd keys for movement ")
  match movement:
    case "w":
      board = merge_up(board)
      game_over = win_check() #check if user has won
      game_over = no_moves()  #check if user lost, can't move
      if game_over:
        break
      if _temp_board != board:
        place_num()
        display()
      else:
        print(f"Movement in {movement} direction not Possible")

    case "a":
      board = merge_left(board)
      game_over = win_check() #check if user has won
      game_over = no_moves()  #check if user lost, can't move
      if game_over:
        break
      if _temp_board != board:
        place_num()
        display()
      else:
        print(f"Movement in {movement} direction not Possible")

    case "s":
      board = merge_down(board)
      game_over = win_check() #check if user has won
      game_over = no_moves()  #check if user lost, can't move
      if game_over:
        break
      if _temp_board != board:
        place_num()
        display()
      else:
        print(f"Movement in {movement} direction not Possible")

    case "d":
      board = merge_right(board)
      game_over = win_check() #check if user has won
      game_over = no_moves()  #check if user lost, can't move
      if game_over:
        break
      if _temp_board != board:
        place_num()
        display()
      else:
        print(f"Movement in {movement} direction not Possible")

    case _:
      print("Invalid Input")
      print("Try Again")