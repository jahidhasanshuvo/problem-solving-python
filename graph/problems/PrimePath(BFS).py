import math

def BFS(node):
    queue = []
    visited[node] = True
    queue.append(node)
    while queue:
        currentNode = queue.pop(0)
        for childNode in graph[currentNode]:
            if not visited[childNode]:
                queue.append(childNode)
                visited[childNode] = True
                steps[childNode] = steps[currentNode] + 1
def validNumber(num1, num2):
    counter = 0
    while num1 > 0:
        if num1%10 != num2%10:
            counter += 1
        num1 = int( num1 / 10)
        num2 = int( num2 / 10)
    if counter<2:
        return True
    return False
def isPrime(number):
    prime = True
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            prime = False
            break
    return prime
graph={}
def findAllPrimeBetween(start, end):
    allPrime = []
    for currentNumber in range(start, end):
        if isPrime(currentNumber):
            allPrime.append(currentNumber)
            graph[currentNumber] = []
    return allPrime
primeNumbers = findAllPrimeBetween(1000,9999)
visited = {}
steps = {}


for i in range(0, len(primeNumbers)):
    firstNode = primeNumbers[i]
    visited[firstNode] = False
    steps[firstNode] = 0
    for j in range(i, len(primeNumbers)):
        secondNode = primeNumbers[j]
        if validNumber(firstNode, secondNode) and firstNode!= secondNode:
            graph[firstNode].append(secondNode)
            graph[secondNode].append(firstNode)

# for i in graph:
#     print(i,"==",graph[i])
# print(graph)

BFS(1373)
print(steps)
print(steps[8017])
