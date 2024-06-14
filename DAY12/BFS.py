graph = {
    5:[7,3],
    7:[5,4,3],
    4:[7,8,2],
    8:[3,4,2],
    3:[5,7,8],
    2:[4,8]
}

# visited = set()
# queue =[5]
# visited.add(5)
# while queue:
#     node = queue.pop(0)
#     print(node,end= " ")
#     for n in graph[node]:
#         if n not in visited:
#             visited.add(n)
#             queue.append(n)

def bfs(visited,queue):
    if not queue:return
    node = queue.pop(0)
    print(node,end= " ")
    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            queue.append(n)
            bfs(visited,queue)
visited =set()
visited.add(5)

bfs(visited,[5])