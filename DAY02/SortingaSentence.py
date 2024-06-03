s =input().split()
mapper = {}
for i in s:
    mapper[int(i[-1])] = i[:len(i)-1]
res =[]
for i in range(1,len(s)+1):
    res.append(mapper[i])
print(" ".join(res))