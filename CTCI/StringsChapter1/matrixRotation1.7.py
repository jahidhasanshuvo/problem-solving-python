size = int(input())
def declareMatrix(size):
    matrix = list()
    for i in range(0, size):
        matrix.append(input().split(' '))
    return matrix
def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
matrix = declareMatrix(size)

# Rotate using transpose and reverse
# for i in range(0, size):
#     for j in range(i, size):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[j][i]
#         matrix[j][i] = temp
# for i in range(0,size):
#     for j in range(0,int(size/2)):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[i][size-j-1]
#         matrix[i][size-j-1] = temp

# Rotate by direct swapping
#             0,0 0,1 0,2 0,3
#             1,0 1,1 1,2 1,3
#             2,0 2,1 2,2 2,3
#             3,0 3,1 3,2 3,3


for i in range(0, int(size/2)):
    for j in range(i,size-i-1):
        top = matrix[i][j]
        matrix[i][j] = matrix[size-j-1][i]
        matrix[size-j-1][i] = matrix[size-i-1][size-j-1]
        matrix[size-i-1][size-j-1] = matrix[j][size-i-1]
        matrix[j][size - i - 1] = top
printMatrix(matrix)
