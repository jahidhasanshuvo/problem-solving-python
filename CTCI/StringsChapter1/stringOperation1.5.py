[str1, str2] = input().split(' ')
str1len = len(str1)
str2len = len(str2)
diff = str1len - str2len
operation = 0
i= 0
j= 0
if diff <=-1 or diff <=1:
    while(i < str1len and j < str2len):
        if(str1[i] != str2[j]):
            operation += 1
            if diff == -1:
                j += 1
            elif diff == 1:
                i+=1
            else:
                i+=1
                j+=1
            if operation>1:
                break
        else :
            i+=1
            j+=1
else:
    print(False)
if operation>1:
    print(False)
else:
    print(True)