arr = list(map(int,input().split()))
n = len(arr)
from collections import Counter
def modifyMEX(arr,n):
    freq = Counter(arr)
    for i in range(n):
        if i not in freq:break
    if i == 0:
        return -1
    else:
        to_be_deleted = -1
        minfreq = -1
        for num in freq:
            if num < i:
                if to_be_deleted == -1 and minfreq == -1:
                    to_be_deleted = num
                    minfreq = freq[num]
                else:
                    if freq[num] < minfreq:
                        to_be_deleted = num
                        minfreq = freq[num]
        return minfreq
res = modifyMEX(arr,n)
print(res)
