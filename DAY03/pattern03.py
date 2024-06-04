# 4
# 1 1 1 1 1 1 1
# 1 2 2 2 2 2 1
# 1 2 3 3 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 3 3 2 1
# 1 2 2 2 2 2 1
# 1 1 1 1 1 1 1
n = int(input())
matrix = []
for i in range(2*n-1):
    matrix.append([0]*(2*n-1))
for i in matrix:
    print(*i)
print(len(matrix[0]), len(matrix))
for i in range(2*n-1):
    for j in range(2*n-1):
        matrix[i][j] = min(2*n-2-i, 2*n-2-j, i, j) + 1
for i in matrix:
    print(*i)
