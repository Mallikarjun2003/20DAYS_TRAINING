# given an array of integers create 2 strings of binary rep.... 
# first str - > for each char its 1 if the char occurs earlier in the arr else 0 
# second str ->for each char its 1 if the char occurs later in the arr else 0 
# nums = [1,3,2,3,4,1] op : 000101 110000  10^4 range
nums = [1,3,2,3,4,1]
s1 = []
s2 =[]
from collections import defaultdict 
freq = defaultdict(int)
for i in nums:
    s1.append(1  if freq.get(i) else 0)
    freq[i]+=1
print(freq)
for i in nums:
    if freq[i] >1:
        freq[i]-=1
        s2.append(1)
    else:
        s2.append(0)
print(s2)


