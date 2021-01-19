def print2D(matrix):
    # print(matrix[2][2])
    for i in matrix:
        for j in i:
            print(j,end=' ')
        print()

array = [[1,2,3,4],[11,22,33,44],[111,222,333,444]]
print2D(array)