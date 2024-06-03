# a = [3,8,5,4,3]
# b=[5,0,9,3,2]
# op : (12 , 17)
def even_sum(even ,idx,n):
    if idx == n:
        return even
    if a[idx]%2 == 0:
        even+=a[idx]
    return even_sum(even,idx+1,n)
    
def odd_sum(odd,idx,m):
    if idx == m:
        return odd
    if b[idx]%2 == 1:
        odd+= b[idx]
    return odd_sum(odd,idx+1,m)
    
a = list(map(int,input().split()))
b = list(map(int,input().split()))
even,odd = 0,0
res = (even_sum(even,0,len(a)), odd_sum(odd,0,len(b)))
print(res)