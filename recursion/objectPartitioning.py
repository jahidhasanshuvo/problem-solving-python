def objectPartition(n,m):
    if n == 0:
        return 1
    elif m == 0 or n<0:
        return 0
    else:
        return objectPartition(n,m-1) + objectPartition(n-m,m)
print(objectPartition(7,4))