# given 2 lists has even and odd nums mixture
# 6 3 2 9 4 7
# 8 7 5 3 6 9
# size are equal
# op:
# generate another list where the even from first list match with odd from odd num 
# eg 6 -> 7, 6 + 7 = 13 6->5 11 ....
# take even num from first list and match with every odd num in second list

nums1 =[6,3,2,9,4,7]
nums2 = [8,7,5,3,6,9]
res =[]
res1= []
def  inner(i,j):
    global res1
    if j == len(nums2):return sum(res1)
    if nums2[j]%2:
        res1.append(nums1[i]+nums2[j])
    inner(i,j+1)
    return sum(res1)

def outer(i):
    global res
    global res1
    if i == len(nums1):return
    if nums1[i]%2 == 0:
        res.append(inner(i,0))
        res1 =[]
    outer(i+1)
outer(0)
print(res)
# odd_nums = sum(num%2 for num in nums2)
# n = len(res)

# # sum_arr= []
# # for i in range(0,n,odd_nums):
# #     sum_arr.append(sum(res[i:i+odd_nums]))
# # print(sum_arr)

# sum_arr=[]
# def sumUp(i,path):
#     if i == n:return
#     if (i+1) % odd_nums==0:
#         sum_arr.append(path+res[i])
#         sumUp(i+1,0)
#     else:
#         sumUp(i+1,path+res[i])
# sumUp(0,0)
# print(sum_arr)