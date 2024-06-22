graph = {
    5 : [(2,2) , (3,2), (8,2)],
    2 : [(5,2), (3,1)] ,
    3 : [(2,1) ,(8,3) ,(5,2),(7,3)],
    8 :[(5,2),(6,4),(3,3)],
    9 :[(6,2),(4,2),(7,1)],
    7 : [(3,3) , (9,1)],
    6 :[(9,2),(8,4)],
    4 :[(9,2)]
}
edges = []
for node in graph:
    for neigh,c in graph[node]:
            edges.append((c,node,neigh))
visited =set()

edges.sort()
print(edges)
path = []
first = edges[0][1]
visited.add(edges[0][1])
from collections import defaultdict
visited_edges =defaultdict(list)
while len(visited) != 8:
    for i in range(len(edges)):
        cost,st,end = edges[i]
        if st in visited and  end not in visited:
            print((st,end))
            visited_edges[st].append(end)
            path.append((st,end))
            visited.add(end)
            break
# print(visited_edges)
# print(path)
