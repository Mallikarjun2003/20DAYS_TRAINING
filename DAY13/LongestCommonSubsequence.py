# ip : asabaab
#     baabab
# find out all subsequences from the given string
s1 = input()
m = len(s1)
s2 = input()
n = len(s2)
# combos = []
# def backtrack(i,path):
#     global combos
#     if i == n:
#         if path:
#             combos.append(path[:])
#         return
#     backtrack(i+1,path+s[i])
#     backtrack(i+1,path)
# backtrack(0,"")
# combos.sort(key = lambda x:len(x))
# print(combos)

dp = [[0]*(n) for _ in range(m)]
for i in range(m):
    for j in range(n):
        if s1[i] == s2[j]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
for row in dp:
    print(*row)

i, j = m-1, n-1
res = ""
while i >= 0 and j >= 0:
    if s1[i] == s2[j]:
        res = s1[i] + res
        i-=1
        j-=1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
print(res)
