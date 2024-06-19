n,m = list(map(int,input().split()))
orow ,ocol = list(map(int,input().split()))
# dir = [(0,1),(1,0)]
# total_ways = 0
# def dfs(i,j):
#     global total_ways
#     if i == n and j == m:
#         total_ways += 1
#         return
#     if i >n and j > m:return
#     for x,y in dir:
#         if 0<=i+x<=n and 0 <=j+y<=m:
#             dfs(i+x,j+y)

# dfs(0,0)
# print(total_ways)
def uniquePaths( m: int, n: int) -> int:
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    total_ways = 0
    def dfs(i,j,visited,path):
        nonlocal total_ways
        if i == n-1 and j == m-1:
            total_ways += 1
            print(path[:])
            return
        if i >=n and j >= m:return
        if (i == orow and j == ocol ) or (i,j) in visited:return
        for x,y in dir:
            if 0<=i+x<n and 0 <=j+y<m:
                visited.add((i,j))
                dfs(i+x,j+y,visited,path +[(i,j)])
        visited.remove((i,j))
    visited = set()
    dfs(0,0,visited,[])
    return total_ways

print(uniquePaths(3,4))


