# ip :
# 4
# t u e d
# f w o w
# r o e r
# d r u i
# word = word
# find if the word is in the word

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
word = input()
dir = [(-1,0) ,(0,-1),(1,0),(0,1)]
m = len(word)
visited =[]
def dfs(r,c,idx):
    if idx == m:
        return True
    if r >= n or c>=n or c < 0 or r<0 or matrix[r][c] != word[idx] or (r,c) in visited:
        return False
    visited.append((r,c))
    for dx,dy in dir:
        if dfs(r+dx,c+dy,idx+1):
            return True
    visited.remove((r,c))
found =False
for row in matrix:
    print(*row)
for i in range(n):
    for j in range(n):
        if matrix[i][j]==word[0]:
            if (dfs(i,j,0)):
                found =True
                print("Yes")
                break
if not found:
    print("No")