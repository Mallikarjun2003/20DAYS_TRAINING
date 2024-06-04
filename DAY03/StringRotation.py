# ip :
# khoor
# 3
# op:
# hello
s = input()
k = int(input())
n = len(s)
letters = "abcdefghijklmnopqrstuvwxyz"
k%=26
res =[]
for i in s:
    char = ord(i) - ord("a") -k
    res.append(letters[char])
print("".join(res))