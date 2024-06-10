nums = [13,9,4,10,5,7]
n = len(nums)

res = []

def recur(idx,maxi_rob):
    
    if idx >= n:
        res.append(maxi_rob)
        return 
    
    recur(idx+2, maxi_rob+ nums[idx])
    recur(idx+1 , maxi_rob)
recur(0,0)
print(max(res))