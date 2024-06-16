# array : [1,4,5] target = 13
arr = [1, 4, 5]
target = 13
dp = [[float("inf")]*(target+1) for _ in range(len(arr) + 1)]
# for i in range(len(arr) + 1):
#     dp[i][0] = 0
# for i in range(1, len(arr) + 1):
#     for wt in range(1, target + 1):
#         if wt < arr[i-1]:
#             dp[i][wt] = dp[i-1][wt]
#         else:
#             dp[i][wt] = min(dp[i-1][wt], 1+dp[i][wt-arr[i-1]])
# for row in dp:
#     print(*row)

one_dp = [float("inf")]*(target+1)
one_dp[0] = 0
for i in arr:
    one_dp[i] = 1
for i in range(1,target+1):
    if i in arr:
        one_dp[i] = min(one_dp[i], 1+one_dp[target-i])
    else:
        one_dp[i] = one_dp[i-1]
print(one_dp)


