'''
input
6 6
0 1
0 2
0 3
1 5
5 2
3 4

input 2
5 5
0 1
0 2
0 3
1 2
3 4
'''
def minimum(a,b):
    return a if a<b else b

def findingBridges(node, parent):
    global timer
    visited[node] = True
    inTime[node] = timer
    lowTime[node] = timer
    timer +=1
    for childNode in graph[node]:
        if not visited[childNode]:
            findingBridges(childNode,node)
            lowTime[node] = minimum(lowTime[node], lowTime[childNode])
        elif childNode!= parent:
            lowTime[node] = minimum(lowTime[node],inTime[childNode])
        if lowTime[childNode] > inTime[node]:
            #print or store the bridge
            print("bridge found=(",childNode,",",node,")")
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
inTime = {}
lowTime = {}
timer = 0
for x in range(0, numberofNodes):
    inTime[x] = -1
    lowTime[x] = -1
    visited[x] = False
while numberOfEdges:
    x,y = input().split(' ')
    x= int(x)
    y= int(y)
    if x not in graph.keys():
        graph[x] = []
    if y not in graph.keys():
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges-=1
print(graph, visited, inTime, lowTime)
findingBridges(0,-1)
print(graph, visited, inTime, lowTime)
