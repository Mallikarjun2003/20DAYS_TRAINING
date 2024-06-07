n = int(input())
k = int(input())
if k == 1:
    print(n)
else:
    for i in range(int(n**0.5+1),-1,-1):
        if n%i == 0:
            k-=1
        if k == 0:
            print(i)
            break
