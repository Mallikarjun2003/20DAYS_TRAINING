graph = {
    5 : [(2,2) , (3,2), (8,2)],
    2 : [(5,2), (3,1)] ,
    3 : [(2,1) ,(8,3) ,(5,2),(7,3)],
    7 : [(3,3) , (9,1)],
    9 :[(6,2),(4,2),(7,1)],
    8 :[(5,2),(6,4),(3,3)],
    6 :[(9,2),(8,4)],
    4 :[(9,2)]
}

start = 5
stack =[5]
path = []
visited = set()
visited.add(5)
while len(visited)<8:
    node = stack.pop()
    # print(node)
    # path.append(node)
    min_edge = float("inf")
    min_node = -1
    parent = -1
    for node in visited:
        for neigh,c in graph[node]:
            if neigh not in visited:
                if c < min_edge:
                    min_node = neigh
                    min_edge = c
                    parent = node
    visited.add(min_node)
    stack.append(min_node)
    path.append((parent,min_node,min_edge))


print(path)