'''
input
9 10
7 1
7 8
7 9
7 4
7 6
5 6
2 3
2 4
3 4
1 2
'''
def initializeVisited(to):
    global visited
    for i in range(1, to + 1):
        visited[str(i)] = False
        distance[str(i)] = 0
def BFS(node):
    visited[node] = True
    queue.append(node)
    while queue:
        currentNode = queue.pop(0)
        for child in graph[currentNode]:
            if not visited[child]:
                visited[child] = True
                distance[child] = distance[currentNode] + 1
                queue.append(child)
                if distance[child] not in dist:
                    dist[distance[child]] = 0
                dist[distance[child]] += 1
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
distance = {}
queue = []
dist = {}
initializeVisited(numberofNodes)
while numberOfEdges:
    x,y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
    if y not in graph.keys():
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges-=1
print(graph, visited)
BFS('7')
targetLevel = 1
print("number of nodes in target level = ",dist[targetLevel])