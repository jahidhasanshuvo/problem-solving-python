def DFS(node, distance):
    global diameter
    global targettedNode
    visited[node] = True
    if diameter<distance:
        diameter = distance
        targettedNode = node
    for child in graph[node]:
        if not visited[child]:
            DFS(str(child), distance+1)
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
targettedNode = -1
diameter = 0
while numberOfEdges:
    x, y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges -= 1
DFS('1',0)
for item in visited:
    visited[item] = False
DFS(str(targettedNode),0)
print(diameter)