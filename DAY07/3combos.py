nums = list(map(int,input().split()))
n = len(nums)
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             print([nums[i],nums[j],nums[k]])

def combine(n, k):
    res = []
    comb = []

    def backtrack(start):
        if len(comb) == k and comb not in res:
            res.append(comb[:])
            return
        for num in range(start, n):
            comb.append(nums[num])
            backtrack(num + 1)
            comb.pop()
    backtrack(0)
    return res
print(combine(n,3))