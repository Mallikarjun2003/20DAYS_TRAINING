from collections import defaultdict

s = input()
window = defaultdict(int)
n = len(s)
l = 0
max_len = 0

for r in range(n):
    window[s[r]] += 1
    while window[s[r]] > 1:
        window[s[l]] -= 1
        if not window[s[l]]:
            del window[s[l]]
        l += 1
    max_len = max(max_len, r-l+ 1)  
print(max_len)
