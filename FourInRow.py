import sys 

EMPTY_SPACE = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = [n for n in range(1,BOARD_WIDTH+1)]

def getNewBoard():
    board = {}
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            board[(i,j)] = EMPTY_SPACE
    return board #this is correct

def displayBoard(boarddict):
    list_val = []
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            list_val.append(boarddict[(j,i)])
    print("""1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|""".format(*list_val)) #* is used to print list with spaces

def askForPlayerMove(playerTurn, boarddict):
    while True: #runs until valid input is made by the player
        playerInput = int(input("Player {}, enter a column or QUIT:".format(playerTurn)))-1
        if(playerInput+1 not in COLUMN_LABELS):
            print("NOT IN LABELS")
            continue
        if(boarddict[(playerInput, 0)]!=EMPTY_SPACE):
            print("NOT EMPTY")
            continue
        
        for j in range(BOARD_HEIGHT-1,-1,-1):
            if(boarddict[(playerInput,j)]==EMPTY_SPACE):
                return (playerInput, j)
#correct
def isFull(boarddict): 
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT):
            if(boarddict[(i,j)]==EMPTY_SPACE):
                return False
    return True 

def isWinner(playerTurn, boarddict):
    #3 nested loops

    #to check if column has 4 elements
    for i in range(BOARD_WIDTH-3):
        for j in range(BOARD_HEIGHT):
            if(boarddict[(i,j)]==playerTurn):
                if(boarddict[(i+1,j)]==playerTurn):
                    if(boarddict[(i+2,j)]==playerTurn):
                        if (boarddict[(i+3,j)]==playerTurn):
                            return True

    #to check if row has same elements
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_HEIGHT-3):
            if(boarddict[(i,j)]==playerTurn):
                if(boarddict[(i,j+1)]==playerTurn):
                    if(boarddict[(i,j+2)]==playerTurn):
                        if (boarddict[(i,j+3)]==playerTurn):
                            return True            
    for i in range(BOARD_WIDTH-3):
        for j in range(BOARD_HEIGHT-3):
            if boarddict[(i,j)]==playerTurn:
                if boarddict[(i+1,j+1)]==playerTurn:
                    if boarddict[(i+2,j+2)]==playerTurn:
                        if boarddict[(i+3,j+3)]==playerTurn:
                            return True
            if boarddict[(i+3,j)]==playerTurn:
                if boarddict[(i+2,j+1)]==playerTurn:
                    if boarddict[(i+1,j+2)]==playerTurn:
                        if boarddict[(i,j+3)]==playerTurn:
                            return True
    return False

def startNewGame():
  print("""WELCOME TO FOUR IN A ROW!""")
  current_board = getNewBoard()
  player = 'X'
  while True: #main game loop
    displayBoard(current_board)
    coordinates = askForPlayerMove(player,current_board)
    current_board[coordinates] = player 

    if (isWinner(player,current_board)==True):
      displayBoard(current_board)
      print("Congratulations {}, You have won!!!".format(player))
      sys.exit()

    elif (isFull(current_board)==True):
      displayBoard(current_board)
      print("It's a tie! GG")
      sys.exit()      

    displayBoard(current_board)
    if player == 'X':
      player = 'O'
    elif player == 'O':
      player = 'X'


startNewGame()