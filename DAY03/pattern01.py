# 3
# * * *
# *  1 *
# * * *
n = int(input())
count = 1
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("*",end=" ")
        else:
            print(count,end=" ")
            count +=1
    print()
