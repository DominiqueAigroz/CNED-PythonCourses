# Create and initialize the array for reversi
colMax = 8 # count of column
rowMax = 8 # count of row

board = []
for idx in range((colMax*rowMax)-1):
    board.append('E')
print(board)

# Simulate input
col = 'c'
row = 2
# Columns starting a
colIndex = ord(col) - ord('a')
print(colIndex)
# Rows starting 1
rowIndex = row - 1
# Calculate the index within our array
index = (rowIndex * colMax) + colIndex
# Test
board[index] = 'W'
print(board)

col = 'b'
row = 3
colIndex = ord(col) - ord('a')
rowIndex = row - 1
index = (rowIndex * colMax) + colIndex
# Test
board[index] = 'B'
print(board)

# Get state
col = 'c'
row = 4
colIndex = ord(col) - ord('a')
rowIndex = row - 1
index = (rowIndex * colMax) + colIndex
# Test
print(board[index])

# Make functions for :
# - Initialize the board
# - Set a state ('E', 'W', 'B') to a column / row
# - Get a state from a column / row