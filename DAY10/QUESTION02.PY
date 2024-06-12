# [4,9,8,2,14,3,5,6]
# (4,9,8),(9,8,2),(14,3,5),(3,5,6) ...
#op:[4, 2, 8, 3, 5, 6, 9, 14]
# unsorted array 
# take the 3 pairs and arrange in the ascending order
nums = [4,9,8,2,14,3,5,6]
n = len(nums)
for i in range(n-2):
    v1,v2,v3 = nums[i],nums[i+1],nums[i+2]
    maxi1 = max(v1,max(v2,v3))
    mini1 = min(v1,min(v2,v3))
    middle = v1+v2+v3-maxi1 -mini1
    nums[i] = mini1
    nums[i+1] = middle
    nums[i+2] = maxi1
print(nums)
    