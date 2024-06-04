nums = list(map(int,input().split()))
l,r = 0,0
n = len(nums)
max_profit = 0
while r<n:
    if nums[r] <= nums[l]:
        l = r
        r = l+1
    else:
        curr_profit = nums[r]- nums[l]
        max_profit = max(max_profit,curr_profit)
        r+=1
print(max_profit)