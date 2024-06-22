# Q.https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3
from collections import defaultdict

s = input()
window = defaultdict(int)
l = 0
n = len(s)
max_str = ""
max_size = 0
for r in range(n):
    window[s[r]] +=1
    while window[s[r]] > 1:
        window[s[l]] -=1
        if not window[s[l]]:del window[s[l]]
        l+=1
    if r - l +1 >max_size:
        max_size = r-l+1
        max_str = s[l:r+1]
print(max_str)
print(max_size)
    
    