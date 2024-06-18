# given an integer n generate an array whose sum is 2^n and the array should have one integer repeating twice and all other are unique
# eg if ip = 3 op can be [1,2,2,3]
from itertools import combinations
n = int(input())
res = []
power_sum = 2**n
combos = combinations(list(range(1,n)),n+1)
