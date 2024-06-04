from collections import Counter
nu=int(input())
l=[]
for i in range(nu):
    l.append(input())
ch=input()
r=0
no=0
count ={}
for i in l:
    count[i] = Counter(i)
for i in range(len(ch)):
    if ch[i] in l[i%nu] and count[l[i%nu]][ch[i]]:
        count[l[i%nu]][ch[i]]-=1
    else:
        no=1
        break
if no:
    print("NO")
else:
    print("YES")