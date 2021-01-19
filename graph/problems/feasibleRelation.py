'''
input for feasible relation
5 5
1 = 2
3 = 1
4 != 2
5 = 4
3 != 5
input for feasible relation
2 2
1 = 2
1 != 2
'''
def initializeVisited(to):
    global visited
    for i in range(1, to + 1):
        visited[str(i)] = False
def findNodeFromRoot(root, target):
    visited[root] = True
    if root == target:
        return True
    else:
        for child in graph[root]:
            if not visited[child]:
                if findNodeFromRoot(child, target):
                    return True
        return False
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
notEqual = []
initializeVisited(numberofNodes)
while numberOfEdges:
    x,y,z = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
    if z not in graph.keys():
        graph[z] = []
    if y == '=':
        graph[x].append(z)
        graph[z].append(x)
    else:
        notEqual.append({x,z})
    numberOfEdges-=1
print(graph, visited, notEqual)
flag = False
for i in notEqual:
    root, target = list(i)
    flag = findNodeFromRoot(root, target)
    break
if flag:
    print("NO")
else:
    print("YES")