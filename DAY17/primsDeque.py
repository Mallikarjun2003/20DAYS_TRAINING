graph = {
    5 : [(2,2) , (3,2), (8,2)],
    2 : [(5,2), (3,1)] ,
    3 : [(2,1) ,(8,3) ,(5,2)],
    7 : [(3,3) , (9,1)],
    9 :[(6,2),(4,2)],
    8 :[(5,2),(6,4),(3,3)],
    6 :[(9,2),(8,4)],
    4 :[(9,2)]
}
import heapq
pq = []
heapq.heapify(pq)
heapq.heappush(pq,(0,5))
visited = set()
visited.add(5)
n = 8

while len(visited)!=n:
    cost,node = heapq.heappop(pq)
    print(node)
    for neig,c in graph[node]:
        if neig not in visited:
            visited.add(neig)
            heapq.heappush(pq,(c,neig))
    

