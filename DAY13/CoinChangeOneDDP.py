arr = [5]
target = 17
dp = [(float("inf"), [])] * (target + 1)
dp[0] = (0, [])
for i in range(1, len(arr) + 1):
    for wt in range(target, 0, -1):
        if wt >= arr[i-1]:
            previous_value = dp[wt-arr[i - 1]]
            if previous_value[0] + 1 < dp[wt][0]:
                dp[wt] = (previous_value[0] + 1, previous_value[1] + [arr[i - 1]])
result = dp[target]
if result[0] != float("inf") and sum(result[1]) == target:
    print(result[0])
else:
    print(-1)
