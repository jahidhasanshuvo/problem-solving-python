
def DFS(node):
    global timer
    visited[node] = True
    inTime[node] = timer
    for child in graph[node]:
        if not visited[child]:
            timer += 1
            DFS(str(child))
    timer+=1
    outTime[node] = timer
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
inTime={}
outTime={}
timer = 1
while numberOfEdges:
    x,y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
        inTime[x] = 0
        outTime[x] = 0
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
        inTime[y] = 0
        outTime[y] = 0
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges-=1
DFS('1')
print(graph, visited)
print(inTime, outTime)