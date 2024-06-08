s =list(input())
print(s)
hash= {}
for i in range(len(s)):
    hash[s[i]] = i
inp = list(input())
inp.sort(key = lambda x:hash[x])
print("".join(inp))