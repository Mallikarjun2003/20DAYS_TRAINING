from collections import defaultdict
graph = defaultdict(list)
end_nodes =[]
while 1:
    st,end = list(input().split("/"))
    if st !="-1":
        graph[st].append(end)
        end_nodes.append(end)
    else:
        break
for node in end_nodes:
    if node not in graph:
        graph[node] = []
max_heirarchy = 0
for node in graph:

    stack = [node]
    visited = set()
    visited.add(node)
    cur_h = 0
    while stack:
        cur_h +=1
        node = stack.pop()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                stack.append(n)
    max_heirarchy = max(max_heirarchy , cur_h-1)
print(max_heirarchy)
