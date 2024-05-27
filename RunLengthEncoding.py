# aaabbaaaddd
s = input()
n = len(s)
prev = s[0]
res= s[0]
count =1
for i in range(1,n):
    if s[i] == prev:
        count +=1
        continue
    res+=str(count)
    count = 1
    prev = s[i]
    res+=prev
res+=str(count)
print(res)
    