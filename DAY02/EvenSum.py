def even_sum(even ,idx,n):
    if idx == n:
        return even
    if a[idx]%2 == 0:
        even+=a[idx]
    return even_sum(even,idx+1,n)
a =range(1,11)
even=0
res = (even_sum(even,0,len(a)))
print(res)