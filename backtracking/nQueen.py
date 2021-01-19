def printBoard(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print()
def validateBoard(board, targetRow, targetCol):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                if targetCol == col or targetRow==row or abs(targetRow-row) == abs(targetCol-col):
                    return False
    return True
def findQueen(board, row, col):
    print("calling-------",board,row,col)
    if row == len(board):
        return True
    else:
        for column in range(len(board)):
            if validateBoard(board, row, column):
                board[row][column] = 1
                printBoard(board)
                print("row,col,column",row,col,column)
                if findQueen(board, row+1, 0):
                    return board
                print(row,col,column)
                board[row][column] = 0
        return False
customNQueen = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = [[0] * 4] * 4
# printBoard(board)
# printBoard(customNQueen)
result = findQueen(customNQueen, 0, 0)
print("------------result---------")
print(result)
# printBoard(result)



# printBoard(customNQueen)
# print(validateBoard(customNQueen, 3,2))
