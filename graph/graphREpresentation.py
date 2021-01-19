numberOfNodes = int(input())
numberOfEdges = int(input())
nodes = {}
while (numberOfEdges):
    x,y = input().split(' ')
    # print(x,y)
    if x not in nodes.keys():
        nodes[x] = []
    if y not in nodes.keys():
        nodes[y] = []
    nodes[x].append(int(y))
    nodes[y].append(int(x))
    numberOfEdges -= 1
print(nodes)
for x in nodes.keys():
    print(nodes[x])
