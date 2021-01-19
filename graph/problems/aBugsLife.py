def DFS(node, type, level):
    if visited[node]:
        if checkType[node] != type:
            print("false return")
            return False
    else:
        visited[node] = True
        checkType[node] = type
        print(node, type)
        for childnode in graph[node]:
            print("childnode",childnode,"type",type,checkType, level)
            if DFS(str(childnode),0 if type == 1 else 1, level+1) == False:
                print("False return in loop",level)
                return False
        print("sobar last a aisi")
        return True

    # visited[node] = True
    # checkType[node] = type
    # for childNode in graph[node]:
    #     if not visited[str(childNode)]:
    #         if DFS(str(childNode),0 if type==1 else 1) == False:
    #             return False
    #     else:
    #         if checkType[node] == checkType[str(childNode)]:
    #             return False
    # return True

numberOfNodes, numberOfEdges = [int(x) for x in input().split(' ')]
graph = {}
visited = {}
distance = {}
checkType = {}

while (numberOfEdges):
    x,y = input().split(' ')
    if x not in graph.keys():
        graph[x] = []
        visited[x] = False
        distance[x] = 0
        # checkType[x] = False
    if y not in graph.keys():
        graph[y] = []
        visited[y] = False
        distance[y] = 0
        # checkType[y] = False
    graph[x].append(int(y))
    graph[y].append(int(x))
    numberOfEdges -= 1
print(graph)
print(DFS('1',0,0))
print(checkType)