inp = input().replace(" ","")
hashset = [False]*26
for i in inp:
    if i.islower():
        hashset[ord(i) - ord("a")] = True
print(sum(hashset) == 26)