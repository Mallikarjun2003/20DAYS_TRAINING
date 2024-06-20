def min_score(n):
    if n == 1:
        return 0
    dp = [float('inf')] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        for j in range(1, int(i **0.5)+1):
            if i % j == 0:
                k = i // j
                dp[i] = min(dp[i], dp[j]+k)
                if j != k:
                    dp[i] = min(dp[i],dp[k]+j)
    
    return dp[n]
n = int(input())
while n !=0:
    print(min_score(n))
    n = int(input())
