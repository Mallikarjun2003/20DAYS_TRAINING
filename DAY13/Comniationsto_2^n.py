# given an integer n generate an array whose sum is 2^n and the array should have one integer repeating twice and all other are unique
# eg if ip = 3 op can be [1,2,2,3] ip 4 op can be 1 2 3 3 7

n = int(input())
res = []
power_sum = 2**n

def dfs(i, path, elements_used):
    if len(path) == n + 1:
        if len(path) - len(set(path)) == 1 and sum(path) == power_sum:
            res.append(path[:])
        return
    if sum(path) > power_sum or i > power_sum:
        return  
    if i not in elements_used or elements_used[i] < 2:
        path.append(i)
        if i in elements_used:
            elements_used[i] += 1
        else:
            elements_used[i] = 1
        dfs(i, path, elements_used)  
        dfs(i+1, path, elements_used) 
        path.pop()
        elements_used[i] -= 1
        if elements_used[i] == 0:
            del elements_used[i]
    dfs(i+1, path, elements_used)
dfs(1, [], {})
print(res)

