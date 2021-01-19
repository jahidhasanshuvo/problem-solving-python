''' input
7 8
3 1
3 2
3 5
2 4
1 2
5 6
5 7
6 7
'''
def BFS(node):
    queue.append(node)
    visited[node] = True
    while queue:
        currentNode = queue.pop(0)
        print(currentNode)
        for childNode in graph[currentNode]:
            if not visited[childNode]:
                queue.append(childNode)
                visited[childNode] = True
                distance[childNode] = distance[currentNode] + 1

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
print(graph, visited)
print("----------result--------")
BFS('3')
print(distance)
print(queue)
