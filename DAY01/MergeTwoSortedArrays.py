# take 2 lists already sorted may or may not be same length 
# Example 
# 2 3 5 7
# 1 3 6 7 10 13
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
n = len(list1)
m = len(list2)
res = [0]*(n+m)
i =j= 0
idx =0
while i < n and j<m:
    if list1[i] < list2[j]:
        res[idx]= list1[i]
        i+=1
    else:
        res[idx] = list2[j]
        j+=1
    idx+=1
while i<n:
    res[idx]= list1[i]
    i+=1
    idx+=1
while j < m:
    res[idx] = list2[j]
    j+=1
    idx+=1
print(res)

    


