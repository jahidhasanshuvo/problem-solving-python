total = int(input())
ans = []
for i in range(0,total):
    x,y = input().split(' ')
    x= int(x)
    y= int(y)
    a,b = 0,0
    previous = 0
    step = 0
    if y>x:
        temp = x
        x=y
        y=temp
    while (a<x or b<y):
        if (previous == 0 or previous == 2 ) and a < x:
            previous = 1
            a+=1
            step+=1
        elif (previous == 1 or previous == 0) and b < y:
            previous= 2
            b+=1
            step+=1
        else:
            previous= 0
            step+=1
    ans.append(step)
for i in range(total):
    print(ans[i])
