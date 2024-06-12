# ip : hello:5438,car:214,book:8799,apple:2187
# op:
# hello ->5438
# if len(hello) in mapped one take 5th char
# car -> 214 here smallest num near to len
# book ->8799 here we dont have smaller than 4 so take x
inp = list(input().split(","))
map = {}
for i in inp:
    st, num = i.split(":")
    map[st] = num
res = ""
for s in map:
    max_int = -1
    l =len(s)
    for n in map[s]:
        if int(n) <= l and int(n) > max_int:
            max_int = int(n)
    res += s[max_int-1] if max_int != -1 else 'x'
print(res)



