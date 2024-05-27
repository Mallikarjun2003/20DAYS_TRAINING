# 3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
# 3 - 4
# 5 - 1
# 4 - 2
# 6 - 1
# 7 - 1
# 1 - 1
# 2 - 1
# 8 - 2
nums = list(map(int,input().split()))
freq = {}
for n in nums:
    freq[n]=freq.get(n,0)+1
for key in freq:
    print(key,"-",freq[key])

