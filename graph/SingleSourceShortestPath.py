def DFS_distance(node, dist):
    if visited[node]:
        return
    else:
        visited[node] = True
        distance[node] = dist
        for adjacentNode in graph[node]:
            DFS_distance(str(adjacentNode), dist+1)
numberOfNodes = int(input())
numberOfEdges = int(input())
graph = {}
visited = {}
distance = {}

while (numberOfEdges):
    x,y = input().split(' ')
    # print(x,y)
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
        distance[x] = 0
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
        distance[y] = 0
    graph[x].append(int(y))
    graph[y].append(int(x))
    numberOfEdges -= 1
print(graph)
DFS_distance('1', 0)
print(visited)
print(distance)