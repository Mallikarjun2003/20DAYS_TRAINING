nums = [4,8,2,4,4,4,8]
# req = len(nums)//2+1
# hashm={}
# for i in nums:
#     hashm[i] = hashm.get(i,0)+1
# for i in hashm:
#     if hashm[i] > req:
#         print(i)
#         break
count = 1
req = nums[0]
for i in nums[1:]:
    if count == 0:
        req = i
    if i == req:
        count +=1
    else:
        count-=1
    
print(req)