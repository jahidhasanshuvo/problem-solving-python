def BFS(node):
    global queue
    visited[node] = True
    queue.append(node)
    while queue:
        currentNode = queue.pop(0)
        print(currentNode)
        for childNode in graph[currentNode]:
            if not visited[childNode]:
                queue.append(childNode)
                visited[childNode] = True
                distance[childNode] = distance[currentNode]+1


numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
distance = {}
queue = []
for i in range(1,numberofNodes+1):
    visited[str(i)] = False
    distance[str(i)] = 0
while numberOfEdges:
    x,y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
    if y not in graph.keys():
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges-=1
BFS('1')
print(distance)