# [2,3,5,6] op : 11
#  we have all coins only 1 is that possible to make target
nums = [2,3,5,6]
target = 11
# found = 0
# for i in range(len(nums)):
#     for j in range(i+2,len(nums)+1):
#         if sum(nums[i:j]) == target:
#             found = 1
#             break
# print(found)

prefix_sums = [0]*len(nums)
prefix_sums[0] = nums[0]
for i in range(1,len(nums)):
    prefix_sums[i] = prefix_sums[i-1]+ nums[i]
n = len(nums)
found = 0
print(prefix_sums)
for i in range(n):
    req = target - prefix_sums[i]
    low = i+1
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if prefix_sums[mid] == req:
            found =1
            break
        elif prefix_sums[mid] < req:
            low+=1
        else:
            high-=1
print(found)


