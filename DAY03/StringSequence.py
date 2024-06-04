# 4
# abcd
# xyze
# pqrw
# stuv

# "cyptdzsayq"
# op:NO
nu=int(input())
l=[]
for i in range(nu):
    l.append(input())
ch=input()
r=0
no=0
for i in ch:
    if i in l[r]:
        r=(r+1)%nu
    else:
        no=1
        break
if no:
    print("NO")
else:
    print("YES")
    
    

    