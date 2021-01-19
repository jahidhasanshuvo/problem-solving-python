counter = 0
def permutation(str, length):
    if len(str) == length:
        global counter
        counter += 1
        print(counter, ''.join(str))
    else:
        for i in range(length, len(str)):
            str[i] , str[length] = str[length], str[i]
            print('else',length,''.join(str))
            permutation(str, length+1)
            print("backtrack", str, length)
            str[length], str[i] = str[i], str[length]
            print("backtrack prev", str, length)

permutation(list("abc"),0)