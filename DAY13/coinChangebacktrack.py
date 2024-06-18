arr = [5]
target = 17
res =[]
def pickNotpick(i,target,path):
    if target<0 or i == len(arr):return
    if target == 0:
        res.append(path[:])
        return
    
    pickNotpick(i,target-arr[i],path+[arr[i]])
    pickNotpick(i+1,target,path)
pickNotpick(0,target,[])
if res:
    print(min(res,key=lambda x:len(x)))
else:
    print(-1)