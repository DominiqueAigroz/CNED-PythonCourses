from functions import *

# The reversi board sizes
colMax = 8 # count of column
rowMax = 8 # count of row

# Create and initialize the array for reversi
#board = initializeBoard(colMax, rowMax)

#initializeGame(board,colMax)

# In one call, I initialize the board and initialize
board = initializeGame2(colMax, rowMax)

# Without a variable
while True:
    col = input('Colonne (a-h): ')
    if col < 'a' or col > 'h':
        print('Veuillez tapez une colonne entre a et h')
    else:
        break

# With a variable
bValid = False
while bValid == False:
    line = int(input('Ligne (1-8): '))
    if line < 1 or line > 8:
        print('Veuillez tapez une ligne entre 1 et 8')
    else:
        bValid = True

if isEmpty(board,col,line,colMax):
    print('is empty')
elif isBlack(board,col,line,colMax):
    print('is black')
elif isWhite(board,col,line,colMax):
    print('is white')

