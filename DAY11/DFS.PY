graph = {
    5:[7,3],
    7:[5,4,3],
    4:[7,8,2],
    8:[3,4,2],
    3:[5,7,8],
    2:[4,8]
}

stack = [5]
visited =set()
visited.add(5)
while stack:
    n = stack.pop()
    print(n,end=" ")
    for node in reversed(graph[n]):
        if node not in visited:
            visited.add(node)
            stack.append(node)
print()
visited =set()
def dfs(node,visited):
    if node and node not in visited:
        print(node,end=" ")

        visited.add(node)
        for n in graph[node]:
            dfs(n,visited)

dfs(5,visited)
