# take a string has m and f only 
# MMFFFMMFMFMF
# if the no of males and no of females are same print 0 else if male is more print m else f
string = input()
ppl = 0
for char in string:
    ppl += 1 if char == "M" else -1
if ppl == 0:
    print(0)
elif ppl<0:
    print("F")
else:
    print("M")