# [3,2,4,1,3,6,7,2]
# op : [[3,2,4,1],[3,6,7,2]]
nums = list(map(int,input().split()))
n = len(nums)
res = []
for i in nums:
    if not res:
        res.append([i])
    else:
        not_found = True
        for row in res:
            if i not in row:
                row.append(i)
                not_found = False
                break
        if not_found:
            res.append([i])
print(res)


