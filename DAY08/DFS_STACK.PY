matrix = []
n = int(input())
for i in range(n):
    matrix.append(list(map(int, input().split())))
start_row = int(input()) - 1
start_col = int(input()) - 1
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
stack = [(start_row, start_col)]

while stack:
    r, c = stack.pop()
    print(r, c)
    if r < 0 or c <0 or c>=n or r >= n or matrix[r][c] == 0: 
        continue
    matrix[r][c] = 0 
    for dx, dy in directions:
        new_row, new_col = r + dx, c + dy
        stack.append((new_row, new_col))
for row in matrix:
    print(*row)
