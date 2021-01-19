str = input()
top = str[0]
count = 1
result = ""
for i in range(1, len(str)):
    count +=1
    if top != str[i]:
        result += '%s%s'%(top,count)
        count = 1
        top = str[i]
result +='%s%s'%(top,count)
print(result) if len(result)<len(str) else print(str)