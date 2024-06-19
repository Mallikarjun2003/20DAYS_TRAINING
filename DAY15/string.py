# ip : tu5g2k1h8
# g5g8gd6h3
# # op: take out all the unique nums 5 2 1 8 6 3  8 6 5 3 1 2
# form the largest possible even number
s1 = input()
s2 = input()
dig = set()
for i in s1:
    if i.isnumeric():
        dig.add(int(i))
for j in s2:
    if j.isnumeric():
        dig.add(int(j))
dig = sorted(list(dig),reverse= True)
min_even = float("inf")
min_odd = float("inf")
for i in dig:
    if i %2 == 0:
        min_even = min(min_even,i)
    elif i %2:
        min_odd = min(min_odd,i)
dig.remove(min_even)
dig.remove(min_odd)
res =""
for i in dig:
    res += str(i)
res+=str(min_odd)+str(min_even)
print(res)
