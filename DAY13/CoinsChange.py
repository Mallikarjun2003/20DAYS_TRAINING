arr = [5]
target = 17
dp = [[(float("inf"),[])]*(target + 1)for _ in range(len(arr) + 1)]
for i in range(len(arr) + 1):
    dp[i][0] = (0, [])
for i in range(1, len(arr) + 1):
    for wt in range(1,target+1):
        dp[i][wt] = dp[i-1][wt]
        if wt >= arr[i-1]:
            previous_value = dp[i][wt-arr[i-1]]
            if previous_value[0] + 1<dp[i][wt][0]:
                dp[i][wt] = (previous_value[0] + 1, previous_value[1] + [arr[i-1]])
row = dp[len(arr)][target]
print(row[0] if sum(row[1]) == target else -1)


