def DFS(node):
    visited[node] = True
    subtreeCount = 1
    for child in graph[node]:
        if not visited[child]:
            subtreeCount += DFS(str(child))
    subtree[node] = subtreeCount
    return subtreeCount
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
subtree = {}
while numberOfEdges:
    x, y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
        subtree[x] = 0
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
        subtree[y] = 0
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges -= 1
print(DFS('1'), subtree)
