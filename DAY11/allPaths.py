visited =set()
res =[]
g = {
    5:[(7,2),(3,1)],
    7:[(5,2),(4,9),(3,4)],
    4:[(7,9),(8,1),(2,4)],
    8:[(3,6),(4,1),(2,4)],
    3:[(5,1),(7,4),(8,6)],
    2:[(4,4),(8,4)]
}
def dfs(node,path,visited,cost,destination):
    if node and node not in visited:
        path.append(node)
        visited.add(node)
        if node == destination:
            # print(path)
            res.append((path[:],cost))
        else:
            for n,ecost in g[node]:
                # print(g[n])
                dfs(n,path,visited,cost +ecost,destination)
        visited.remove(node)
        path.pop()
for i in g.keys():
    for j in g.keys():
        if i != j:
            print(f"All paths from {i} to {j}:\n")
            source = i
            destination = j
            visited = set()
            res = []
            dfs(source, [], visited, 0, destination)
            for path, cost in res:
                print(f"Path: {path}, Cost: {cost}")

