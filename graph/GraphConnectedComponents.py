def DFS(node):
    if visited[node]:
        return
    else:
        visited[node] = True
        for child in graph[node]:
            DFS(str(child))
def connectedComponents():
    connected = 1
    for node in visited:
        if visited[node] == False:
            DFS(node)
            connected += 1
    return connected
numberOfNodes = int(input())
numberOfEdges = int(input())
graph = {}
visited = {}
inVisited = 0
while (numberOfEdges):
    x,y = input().split(' ')
    # print(x,y)
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
        inVisited +=1
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
        inVisited +=1
    graph[x].append(int(y))
    graph[y].append(int(x))
    numberOfEdges -= 1
print(graph)
DFS('1')
print(visited)
print(connectedComponents() - inVisited + numberOfNodes)
