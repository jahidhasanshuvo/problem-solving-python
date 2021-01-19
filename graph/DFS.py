def DFS(node):
    if visited[node]:
        return
    else:
        print(node)
        visited[node] = True
        for child in graph[node]:
            DFS(str(child))


numberOfNodes = int(input())
numberOfEdges = int(input())
graph = {}
visited = {}
while (numberOfEdges):
    x,y = input().split(' ')
    # print(x,y)
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
    graph[x].append(int(y))
    graph[y].append(int(x))
    numberOfEdges -= 1
print(graph)
DFS('2')
