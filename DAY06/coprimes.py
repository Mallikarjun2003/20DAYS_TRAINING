n , m = list(map(int,input().split()))
coprimes = 1
for i in range(2,max(n,m)):
    if n%i == 0 and m%i == 0:
        coprimes =0
if coprimes:
    print("Yes")
else:
    print("NO")

