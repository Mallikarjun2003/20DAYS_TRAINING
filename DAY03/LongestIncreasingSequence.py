# xyzabcdefklmnopqefgh
s = input()
max_length = 0
curr_max = 1
n= len(s)
for i in range(1,n):
    if ord(s[i]) - ord(s[i-1]) ==1:
        curr_max+=1
    else:
        max_length = max(max_length,curr_max)
        curr_max = 1
print(max(max_length,curr_max))