nums = [13,9,4,10,5,7]
n = len(nums)
# i = 2
# dp =[0]*(n)
# dp[0] = nums[0]
# dp[1] = max(nums[1],nums[0])

# for i in range(2,n):
#     dp[i] = max(dp[i-2]+nums[i] , dp[i-1])
# print(dp[n-1])
res = []

def recur(idx,maxi_rob):
    
    if idx >= n:
        res.append(maxi_rob)
        return 
    recur(idx+2, maxi_rob+ nums[idx])
    recur(idx+1 , maxi_rob)
recur(0,0)
print(max(res))