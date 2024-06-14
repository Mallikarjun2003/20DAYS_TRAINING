g = {
    0 :[(0,0),(1,1),(2,2)],
    1:[(0,1),(2,4),(3,6)],
    2:[(4,9),(1,4),(0,2)],
    3:[(1,6),(4,1),(5,4)],
    4:[(3,1) ,(5,4),(2,9)],
    5:[(4,4),(3,4)]
}

dist = [float("inf")]*6

dist[0] =0
import heapq
heap = []
heapq.heapify(heap)
visited = set()
visited.add(0)
heapq.heappush(heap,(0,0))
while heap:
    node,cost = heapq.heappop(heap)
    for neigh,cost in g[node]:
        dist[neigh] = min(dist[neigh],cost + dist[node])
        if neigh not in visited:
            visited.add(neigh)
            heapq.heappush(heap,(neigh,dist[neigh]))
print(dist)

