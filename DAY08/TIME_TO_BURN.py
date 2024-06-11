from collections import deque

def bfs(matrix, start_row, start_col, time_per_tree):
    n = len(matrix)
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque([(start_row, start_col, 0)])  
    visited = set()
    visited.add((start_row, start_col))
    max_time = 0
    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)

        for dx, dy in directions:
            new_r, new_c = r + dx, c + dy
            if 0 <= new_r < n and 0 <= new_c < n and matrix[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                matrix[new_r][new_c] = 0  
                queue.append((new_r, new_c, time + time_per_tree))
    
    return max_time

n = int(input())  
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

start_row = int(input()) - 1  
start_col = int(input()) - 1  
time_per_tree = int(input()) 
time_to_stop = bfs(matrix, start_row, start_col, time_per_tree)
print(time_to_stop)

# Sample Input:
# 6
# 0 1 1 1 0 1
# 0 1 0 1 0 0
# 1 0 0 1 0 0
# 0 0 0 1 1 1
# 1 1 0 0 0 1
# 1 1 1 0 1 0
# 4
# 6
# 1
