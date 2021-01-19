def pathCount(n,m):
    if n==1 or m==1:
        return 1
    else:
        print(n,m)
        return pathCount(n-1,m) + pathCount(n, m-1)

print(pathCount(3,3))