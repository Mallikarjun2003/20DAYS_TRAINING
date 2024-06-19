# [2,3,5,6] op : 11
#  we have all coins only 1 is that possible to make target
nums = [2,3,5,6]
target = 7


# table =[[0]*(target+1) for _ in range(len(nums))]
# for i in range(len(nums)):
#     table[i][0] = 1
# for i in range(len(nums)):
#     for j in range(1,target+1):
#         if j == nums[i]:table[i][j] = 1
#         if j > nums[i] :
#             table[i][j] = 0 if i == 0 else table[i-1][j]
        




