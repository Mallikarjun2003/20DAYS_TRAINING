# ip:"school"
#     3
#     L 2 means to rotate leftside 2 times - >hoolsc 
#     R 3 - >oolscl 
#     L 1 ->chools
# hoc
# op:
#check whether the substring so formed has an anagram in the string
from collections import Counter
s = input()
t = int(input())
n = len(s)
sum =0
res = []
for _ in range(t):
    dir , k = input().split()
    k = int(k)
    
    if dir == "L":
        sum += k
        res.append(s[sum])
    else:
        sum-=k
        res.append(s[sum])

count = Counter(res)
found = False
j = 0

for i in range(0,n-t):
    if j == t:
        found = True
        break
    if s[i] == res[j]:
        j+=1
if found:
    print()
        