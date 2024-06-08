n = int(input())

# def prime(num):
#     if num == 1:
#         return True
#     for i in range(2, int(num**0.5)+1):
#         if num%i == 0:
#             return False
#     return True
# can_sum = False

# for i in range(1,n):
#     if prime(i) and prime(n -i):
#         can_sum =True
#         break
# print(can_sum)

primes = [True]*(n)
for i in range(2,n):
    if primes[i]:
        for j in range(i*2,n,i):
            primes[j]= False
can_sum =False
for i in range(1,n):
    if primes[i] and primes[i-1]:
        can_sum =True
        break
print("Yes") if can_sum else print("No")
