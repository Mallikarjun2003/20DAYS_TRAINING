# ip:increasing array [4,8,14,22,36,68] primes btwn the pairs is 
# (4,8) - 7
# (8,14) - 13
# (14,22) -19
# (22,36)-31
# (36,68) - 67
# all the ele in arr are non prime and in increasing order
# take pair of elements each time and find the largest prime in that range
#sum of all the primes is the op
nums = [14,16,20,22]
sum = 0
def prime(num1,num2):
    for num in range(num2,num1,-1):
        found=False
        for j in range(2,num//2+1):
            if num %j==0:
                found = True
        if not found:
            print(num)
            return num
    return 0
for i in range(len(nums)-1):
    sum+=prime(nums[i],nums[i+1])
print(sum)
        