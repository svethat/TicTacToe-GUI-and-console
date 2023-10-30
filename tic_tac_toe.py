'''
program to play game Tic Tac Toe bwteen two players

'''

# importing the requiRED modules
import sys
import pygame
import time

# init
pygame.init()


# colour variables used
BG_COLOR = (20,189,172)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
CIRCLE_COLOR = (239, 231, 200)


# screen dimentions and related variables

WIDTH = 600
HIEGHT = 600

CELL_SIZE = WIDTH/3

space = int(CELL_SIZE*0.75)
space_x = int(CELL_SIZE*0.25)

line_width = 10

# initializing game variables

board = [["-","-","-"],
         ["-","-","-"],
         ["-","-","-"]]

player = 'X'

GAME_IS_GOING = True

# setting up game screen
screen=pygame.display.set_mode((WIDTH,HIEGHT))

# adding title and icon
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

icon= pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

# for restart button
v_rect = pygame.Rect(150,150,600,100) 

def draw_grid():
	# draw the dividing lines
	pygame.draw.line(screen,WHITE,(0,CELL_SIZE),(WIDTH,CELL_SIZE),line_width)
	pygame.draw.line(screen,WHITE,(0,CELL_SIZE*2),(WIDTH,CELL_SIZE*2),line_width)		
	pygame.draw.line(screen,WHITE,(CELL_SIZE,0),(CELL_SIZE,WIDTH),line_width)	
	pygame.draw.line(screen,WHITE,(CELL_SIZE*2,0),(CELL_SIZE*2,WIDTH),line_width)	


def mark_position(x,y,player):

	if board[x][y]=='-': # check to make sure the cell is available for marking
		board[x][y]= player

	if player == 'O':
		pygame.draw.circle(screen, CIRCLE_COLOR, (int(board_cell_x * CELL_SIZE +CELL_SIZE/2), int(board_cell_y * CELL_SIZE + CELL_SIZE/2)),(space/2) , 15)
		
	else:
		
		pygame.draw.line(screen, BLACK, (int(board_cell_x * CELL_SIZE + CELL_SIZE/2 - space_x), int(board_cell_y * CELL_SIZE+CELL_SIZE/2 -space_x ))\
			,(int(board_cell_x * CELL_SIZE + CELL_SIZE/2 + space_x), int(board_cell_y * CELL_SIZE+CELL_SIZE/2) + space_x) , line_width)
			
		pygame.draw.line(screen, BLACK, (int(board_cell_x * CELL_SIZE + CELL_SIZE/2 + space_x), int(board_cell_y * CELL_SIZE+CELL_SIZE/2 -space_x ))\
			,(int(board_cell_x * CELL_SIZE + CELL_SIZE/2 - space_x), int(board_cell_y * CELL_SIZE+CELL_SIZE/2) + space_x) , line_width)

# check if game is over

def is_board_full():
	for row in range(3):
		for col in range(3):
			if board[row][col] == '-':
				return False

	return True


# check for horizontal match
def check_rows(player):
	global GAME_IS_GOING

	row1 = board[0][0]==board[1][0]==board[2][0] != '-'
	row2 = board[0][1]==board[1][1]==board[2][1] != '-'
	row3 = board[0][2]==board[1][2]==board[2][2] != '-'

	if row1:
		victory_linex(x=0)
	elif row2:
		victory_linex(x=1)
	elif row3:
		victory_linex(x=2)
	pygame.display.update()
	time.sleep(0.5)	

	if row1 or row2 or row3:
		GAME_IS_GOING=False
		display_winner(player)

# check for vertical match
def check_cols(player):
	global GAME_IS_GOING
	y=0

	col1 = board[0][0]==board[0][1]==board[0][2] != '-'
	col2 = board[1][0]==board[1][1]==board[1][2] != '-'
	col3 = board[2][0]==board[2][1]==board[2][2] != '-'

	if col1:
		victory_liney(y=0)
	elif col2:
		victory_liney(y=1)
	elif col3:
		victory_liney(y=2)
	pygame.display.update()
	time.sleep(0.5)

	if col1 or col2 or col3:
		GAME_IS_GOING=False
		display_winner(player)
	

  
# check for diagobal match
def check_diagonals(player):
  '''
  0 | 1 | 2 | 
  3 | 4 | 5 | 
  6 | 7 | 8 |
  to check horizontal match, check if same player has 
  marked in positions 0,4,6 or 2,4,6  
  '''
  global GAME_IS_GOING
  diagonal1 = board[0][0]==board[1][1]==board[2][2] != "-"
  diagonal2 = board[0][2]==board[1][1]==board[2][0] != "-"
  

  if diagonal1:
  	pygame.draw.line(screen,RED,(0, 0),(WIDTH, WIDTH),line_width)
  elif diagonal2:
    pygame.draw.line(screen,RED,(0, WIDTH),(WIDTH, 0),line_width)

  pygame.display.update()
  time.sleep(0.5)

  if diagonal1 or diagonal2:
    GAME_IS_GOING=False
    display_winner(player)



def victory_liney(y=0):
	pygame.draw.line(screen,RED,(int(y * CELL_SIZE + CELL_SIZE/2), 0),(int(y * CELL_SIZE + CELL_SIZE/2), WIDTH),10)

def victory_linex(x=0,y=0):
	pygame.draw.line(screen,RED,(0,int(x * CELL_SIZE + CELL_SIZE/2)),(WIDTH,int(x * CELL_SIZE + CELL_SIZE/2)),10)
	# to do restart game and screen display

def check_for_winner(player):
	global GAME_IS_GOING

	check_cols(player)
	check_rows(player)
	check_diagonals(player)
	if is_board_full() and GAME_IS_GOING:
		display_draw()

def display_winner(player):
	screen.fill(BG_COLOR)
	if player == 'O':
			pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH // 2,WIDTH // 2),200 , 20)
		
	else:	
			pygame.draw.line(screen, BLACK, (CELL_SIZE,CELL_SIZE),(CELL_SIZE *2,CELL_SIZE *2) , 15)
				
			pygame.draw.line(screen, BLACK, (CELL_SIZE,CELL_SIZE *2),(CELL_SIZE *2,CELL_SIZE) , 15)

	font = pygame.font.Font(None,50) # 100 is for font size
	location =(CELL_SIZE,750)
	screen.blit(font.render("WINNER!!", True,RED),location)
	
	# restart game option
	pygame.draw.rect(screen, BG_COLOR, v_rect)
	screen.blit(font.render("RESTART GAME",True,WHITE),(150,150))

def display_draw():
	screen.fill(BG_COLOR)
	pygame.draw.circle(screen, CIRCLE_COLOR, (250,550),CELL_SIZE // 2 , 20)	
	pygame.draw.line(screen, BLACK, (CELL_SIZE *2-space_x,CELL_SIZE+space_x),(WIDTH-space_x,CELL_SIZE *2+space_x) , 15)			
	pygame.draw.line(screen, BLACK, (WIDTH-space_x,CELL_SIZE+space_x),(CELL_SIZE *2-space_x,CELL_SIZE *2+space_x) , 15)

	font = pygame.font.Font(None,100)
	location =(CELL_SIZE,750)
	screen.blit(font.render("DRAW!!", True,RED),location)
	# restart game option
	pygame.draw.rect(screen, WHITE, v_rect)
	screen.blit(font.render("RESTART GAME",True,WHITE),(150,150))

draw_grid()

## main game loop

while True:
	
	for event in pygame.event.get() :
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and GAME_IS_GOING:
			draw_grid()
			x = event.pos[0]
			y = event.pos[1]

			board_cell_x = int(x//CELL_SIZE)
			board_cell_y = int(y//CELL_SIZE)

			if player == 'O':
				mark_position(board_cell_x,board_cell_y,player)
				check_for_winner(player)
				player ='X' # switch the turn
			else:
				mark_position(board_cell_x,board_cell_y,player)
				check_for_winner(player)
				player ='O' # switch the turn

		if event.type == pygame.MOUSEBUTTONDOWN and not GAME_IS_GOING:
			pos = pygame.mouse.get_pos()
			if v_rect.collidepoint(pos):
				screen.fill(BG_COLOR)
				draw_grid()
				board = [["-","-","-"],
						 ["-","-","-"],
						 ["-","-","-"]]

				player = 'X'
				GAME_IS_GOING = True


	pygame.display.update()


