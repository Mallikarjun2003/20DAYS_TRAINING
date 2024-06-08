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
res = []
for _ in range(t):
    dir , k = input().split()
    k = int(k)
    if dir == "L":
        res.append(s[k])
    else:
        res.append(s[-k])
count = Counter(res)
found = False
for i in range(0,n-t):
    count_t= Counter(s[i:i+t])
    if count == count_t:
        found= True
        print("yes")
if not found:
    print("NO")