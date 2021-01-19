def cycleDetect(node, parent):
        visited[node] = True
        print(node)
        for child in graph[node]:
            if not visited[child]:
                if cycleDetect(str(child), node):
                    return True
            elif child!=parent:
                return True
        return False
numberofNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
while numberOfEdges:
    x,y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
    graph[x].append(y)
    graph[y].append(x)
    numberOfEdges-=1
print(graph, visited)
print(cycleDetect('1','-1'))