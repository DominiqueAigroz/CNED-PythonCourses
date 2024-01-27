# This is the module for the reversi game

def initializeBoard(colSize,rowSize):
    arr = []
    for idx in range((colSize*rowSize)-1):
        arr.append('E')
    return arr

def setState(arr,col,row,colMax,color):
    # Columns starting a
    colIndex = ord(col) - ord('a')
    # Rows starting 1
    rowIndex = row - 1
    # Calculate the index within our array
    index = (rowIndex * colMax) + colIndex
    # Assigns the color to the cell
    arr[index] = color

def getState(arr,col,row,colMax):
    # Columns starting a
    colIndex = ord(col) - ord('a')
    # Rows starting 1
    rowIndex = row - 1
    # Calculate the index within our array
    index = (rowIndex * colMax) + colIndex
    # Retrieve the color on the cell
    return arr[index]

def isEmpty(arr,col,row,colMax):
    return getState(arr,col,row,colMax) == 'E'

def isBlack(arr,col,row,colMax):
    return getState(arr,col,row,colMax) == 'B'

def isWhite(arr,col,row,colMax):
    return getState(arr,col,row,colMax) == 'W'

def initializeGame(arr,colMax):
    setState(arr,'d',4,colMax,'W')
    setState(arr,'e',4,colMax,'B')
    setState(arr,'d',5,colMax,'B')
    setState(arr,'e',5,colMax,'W')

def initializeGame2(colSize,rowSize):
    arr = initializeBoard(colSize,rowSize)
    setState(arr,'d',4,colSize,'W')
    setState(arr,'e',4,colSize,'B')
    setState(arr,'d',5,colSize,'B')
    setState(arr,'e',5,colSize,'W')
    return arr


def inputColumn():
    return 

def inputLine():
    return 