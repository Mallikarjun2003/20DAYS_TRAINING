# ip : 6 
# 0 1 1 1 0 1
# 0 1 0 1 0 0
# 1 0 0 1 0 0
# 0 0 0 1 1 0
# 1 1 0 0 0 1
# 1 1 1 0 1 0
# 1 ->Trees 
# 0 -> bare lands

# (4,6) - > catches fire 
# dir top ,left ,right ,Down
# op:
# return the number of saved trees
matrix = []
n = int(input())
for i in range(n):
    matrix.append(list(map(int,input().split())))
start_row = int(input())
start_col = int(input()) -1
rows = len(matrix[0])
dir = [(-1,0) ,(0,-1),(1,0),(0,1)]
visited =set()
def dfs(r,c,matrix):

    if r >= n or c>=n or c < 0 or r<0 or (r,c) in visited or matrix[r][c] == 0:
        return
    elif (r,c) not in visited:
        visited.add((r,c))
        if matrix[r][c]:
            print((r,c))
            matrix[r][c] = 0
            for dx ,dy in dir:
                dfs(r+dx, c+dy,matrix)
        visited.remove((r,c))
dfs(start_row,start_col,matrix)
res = 0
for row in matrix:
    print(*row)
for row in matrix:
   res += sum(row)
print(res)        
"""
6
0 1 1 1 0 1
0 1 0 1 0 0
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0
4
6
"""