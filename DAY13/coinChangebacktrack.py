arr = [1, 4, 5]
target = 13
res =[]
def pickNotpick(i,target,path):
    if target<0 or i == 3:return
    if target == 0:
        res.append(path[:])
        return
    
    pickNotpick(i,target-arr[i],path+[arr[i]])
    pickNotpick(i+1,target,path)
pickNotpick(0,target,[])

print(min(res,key= lambda x:len(x)))