''' 
### Tic Tac Toe game for two playes ###
'''

# board layout

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# declare global variables
game_is_going = True       
winner = None
current_player="X"


# display board on the screen
def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2]+" | ")   
  print(board[3]+" | "+board[4]+" | "+board[5]+" | ")
  print(board[6]+" | "+board[7]+" | "+board[8]+" | ")    

# check for horizontal match
def check_rows():
  global game_is_going
  
  '''
  0 | 1 | 2 | 
  3 | 4 | 5 | 
  6 | 7 | 8 |
  to check horizontal match, check if same player has 
  marked in positions 0,1,2 or 3,4,5 or 6,7,8. 
  
  '''

  row1 = board[0]==board[1]==board[2] != "-"
  row2 = board[3]==board[4]==board[5] != "-"
  row3 = board[6]==board[7]==board[8] != "-"

  if row1 or row2 or row3:
    game_is_going=False

  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]    
  
# check for vertical match
def check_columns():
  '''
  0 | 1 | 2 | 
  3 | 4 | 5 | 
  6 | 7 | 8 |
  to check horizontal match, check if same player has 
  marked in positions 0,3,6 or 1,4,7 or 2,5,8. 
  
  '''
  global game_is_going

  column1 = board[0]==board[3]==board[6] != "-"
  column2 = board[1]==board[4]==board[7] != "-"
  column3 = board[2]==board[5]==board[8] != "-"


  if column1 or column2 or column3:
    game_is_going=False

  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]    
  
# check for diagobal match
def check_diagonals():
  '''
  0 | 1 | 2 | 
  3 | 4 | 5 | 
  6 | 7 | 8 |
  to check horizontal match, check if same player has 
  marked in positions 0,4,6 or 2,4,6  
  
  '''
  
  global game_is_going
  diagonal1 = board[0]==board[4]==board[8] != "-"
  diagonal2 = board[2]==board[4]==board[6] != "-"
  

  if diagonal1 or diagonal2:
    game_is_going=False

  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]

def check_for_winner():

  global winner
  
  # check for any winning match
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  
  # if match found assign the winner
  if row_winner:
    winner=row_winner
  elif column_winner:
    winner=column_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    winner=None
    

# check for end of game 
def check_end_of_game():
  global game_is_going
  if "-" not in board:
    game_is_going=False
    
      
# change the turn of the player
def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"  
  

# check if game ended
def check_if_game_over():
  check_for_winner()
  check_end_of_game()


def handle_turn(player):
  '''
    this functions accepts a players input and validates the input received

    Parameters
    ----------
    player : only 'X' or 'O' permitted
    Returns
    -------
    None.

  '''
  print(" \n"+player+"'s turn.")
  position  = input("Please enter a number 1-9: ")

  valid = False
  while not valid:
    
    while position not in ["1","2","3","4","5","6","7","8","9"]:

      position=input("Invalid input!! \n Please enter a different number: ")

    position=int(position)-1

    if board[position] == '-':
      valid=True
    else:  
     print("This position is already taken!! \n Choose a different number: ")

  board[position]= player
  
  ## display the board with new positions 
  display_board()

###############################################################################
###############################################################################

### playing the game ####

def lets_play():
  ## display the board at the start of the game 
  display_board()

  while game_is_going:
      handle_turn(current_player)

      check_if_game_over()

      flip_player()

  if winner == "X" or winner =="O":
   print ('CONGRAGULATIONS!!!')
   print(winner+" Won!!!")
  else:
   print("It's a tie!!")   
 
lets_play()