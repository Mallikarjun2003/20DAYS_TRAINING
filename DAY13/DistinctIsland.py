# 0 1 0 0 1
# 1 0 0 1 1
# 0 0 0 0 0
# 1 0 0 0 0
# 1 0 0 0 1
mat = [[0,1,0,0,1],
       [1,0,0,1,1],
       [0,0,0,0,0],
       [1,0,0,0,0],
       [1,0,0,0,1]]
rows = cols = 5  
dir = [(0,-1),(-1,0),(1,0),(0,1)] 
# print the number of islands in the graph
def dfs(i,j,visited):
    if i == rows or j == cols or i <0 or j<0 or (i,j) in visited or mat[i][j] == 0:
        return 0
    mat[i][j] = 0
    co=1
    visited.add((i,j))
    for dx,dy in dir:
        new_x ,new_y = i+dx,j+dy
        if 0<=new_x <rows and 0<=new_y<cols:
            co+= dfs(new_x,new_y,visited)
    return co

max_area = 0 
is_lands = 0
visited =set()
for r in range(rows):
    for c in range(cols):
        if mat[r][c]:
            is_lands+=1
            max_area = max(max_area,dfs(r,c,visited))

print(is_lands)
print(max_area)
