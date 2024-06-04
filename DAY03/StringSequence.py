# 4
# abcd
# xyze
# pqrw
# stuv

# "cyptdzsayq"
# op:NO
n = int(input())
alpha = []
for i in range(n):
    alpha.append(list(input()))
s = input()
st = []
for i in s:
    for idx,j in enumerate(alpha):
        if i in j:
            st.append(idx)
print(st)
found = True
for i in range(1,len(st)):
    if st[i] == n-1:
        continue
    if st[i] - st[i-1] !=1:
        found=False
        break
    
    

    