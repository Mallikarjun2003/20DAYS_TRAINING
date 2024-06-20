# inp = input()
# n = len(inp)
# # max_length = -1
# # max_str = ""
# # for i in range(n):
# #     for j in range(i+2,n+1):
# #         if inp[i:j] == inp[i:j][::-1] and j-i > max_length:
# #             # print(inp[i:j])
# #             max_length = len(inp[i:j])
# #             max_str = inp[i:j]
# # print(max_str)
# def centre_expand(l,r,n):
#     while l >= 0 and r < n:
#         if inp[l] == inp[r]:
#             l-=1
#             r+=1
#         else:
#             return inp[l+1:r]
#     return inp[l+1:r]

# if n%2:
#     mid = n//2
#     print(centre_expand(mid-1 ,mid+1,n))
# else:
#     mid= n//2
#     inp = inp[:mid]+"0"+inp[mid:]
#     res = centre_expand(mid-1 ,mid+1,n+1)
#     mid == len(res)//2
#     print(res[:mid]+res[mid+1:])
s = input()
n = len(s)
def centre_expand(l, r):
    while l >= 0 and r <n and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]

longest = ""
for i in range(n):
    p1 = centre_expand(i,i)
    p2 = centre_expand(i,i+1)
    if len(p1) > len(longest):
        longest = p1
    if len(p2) > len(longest):
        longest = p2tp
print(longest)

