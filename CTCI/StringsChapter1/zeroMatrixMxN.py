[row, column] = [int(x) for x in input().split(' ')]
def declareMatrix(row, column):
    matrix = list()
    for i in range(0, row):
        matrix.append(input().split(' '))
    return matrix
def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
matrix = declareMatrix(row,column)
zeroRow = []
zeroColumn = []
for i in range(0,row):
    for j in range(0, column):
        if matrix[i][j] == '0':
            zeroRow.append(i)
            zeroColumn.append(j)
for i in zeroRow:
    for j in range(0, len(matrix[i])):
        matrix[i][j] = 0
for i in range(0, row):
    for j in zeroColumn:
        matrix[i][j] = 0
printMatrix(matrix)