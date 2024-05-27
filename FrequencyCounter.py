# loveLOVE
# lv -2
# uv - 2
# lc - 
# uc - 
# d - 
# sp -
lower_vowels = set(["a","e","i","o","u"])
upper_vowels = set(["A","E","I","O","U"])
lower_cons = set(list("bcdfghjklmnpqrstvwxyz"))
upper_cons = set(list("BCDFGHJKLMNPQRSTVWXYZ"))
digits =set(list("0123456789"))
lv = uv = lc = uc = d = spl = 0
inp= input()
for i in inp:
    if i in lower_vowels:
        lv+=1
    elif i in upper_vowels:
        uv +=1
    elif i in lower_cons:
        lc+=1
    elif i in upper_cons:
        uc+=1
    elif i in digits:
        d+=1
    else:
        spl+=1
print(lv,uv,lc,uc,d,spl)
