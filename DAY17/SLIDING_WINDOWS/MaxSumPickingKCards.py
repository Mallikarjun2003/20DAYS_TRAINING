# Q. https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)


l = k-1
r = n-1
l_sum = sum(arr[:k])
r_sum = 0
max_sum = l_sum + r_sum
for i in range(k):
    print(l_sum , r_sum)
    l_sum -= arr[l]
    r_sum += arr[r]
    print(l_sum , r_sum)
    max_sum = max(max_sum ,l_sum + r_sum)
    l-=1
    r-=1
print(max_sum)



