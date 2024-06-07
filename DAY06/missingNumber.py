# 7
# 0 5 3 6 7 2 1
# 4
nums = list(map(int,input().split()))
n = len(nums)
print(n*(n+1)//2 - sum(nums))