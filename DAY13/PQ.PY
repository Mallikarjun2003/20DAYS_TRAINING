# ip : 2 lists given to u 
# list data are timings 
# job timings = [(1,3),(2,5),(4,6),(3,7),(5,8),(7,9)]
# profits = [5,6,5,20,11,2]
# op:print the max profit 17
job_timings = [(1,3),(2,5),(4,6),(3,7),(5,8),(7,9)]
profits = [5,6,5,20,11,2]
n = len(profits)
for i in range(n-1):
    for j in range(n-1-i):
        if job_timings[j][0] > job_timings[j+1][0]:
            profits[j], profits[j+1] = profits[j+1], profits[j]
            job_timings[j], job_timings[j+1] = job_timings[j+1], job_timings[j]
print(job_timings)
profit_table = {}
for i in range(n):
    profit_table[job_timings[i]] = profits[i]
    

max_p = 0
for i in range(n):
    prev_end = 0
    profit = 0
    for st,end in job_timings[i:]:
        if st >=prev_end:
            # print(st,end,profit_table[(st,end)])
            prev_end = end
            profit += profit_table[(st,end)]
    max_p = max(max_p,profit)
print(max_p)