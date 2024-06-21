pods = [8,6,8]
costs = [9,5,7]
pair_wise = [(costs[i] , pods[i]) for i in range(3)]
n = 3
from collections import Counter
pair_wise.sort()
print(pair_wise)
# freq = Counter(pods)
# cost = 0
# for i in range(n):
#     if freq[pods[i]] >1:
#         cost += costs[i]
#         freq[pods[i]] -=1
#         if pods[i]+1 in freq:
#             freq[pods[i]+1] +=1
#         else:
#             freq[pods[i]+1] =1
# print(cost)


