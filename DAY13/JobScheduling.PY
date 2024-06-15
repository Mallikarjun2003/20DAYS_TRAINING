# ip : 2 lists given to u 
# list data are timings in ascending order
# job timings = [(1,3),(2,5),(4,6),(3,7),(5,8),(7,9)]
# profits = [5,6,5,20,11,2]
# [(1, 3), (2, 5), (4, 6), (5, 8), (6, 7), (7, 9)]
# [5, 6, 5, 11, 4, 2] op : 17
# op:print the max profit 27
job_timings = [(1,3),(2,5),(4,6),(3,7),(5,8),(7,9)]
profits = [5,6,5,20,11,2]
n = len(profits)
profit_table = {}
for i in range(n):
    profit_table[job_timings[i]] = profits[i]
    
max_p = 0
for i in range(n):
    prev_end = 0
    profit = 0
    for st,end in job_timings[i:]:
        if st >=prev_end:
            prev_end = end
            profit += profit_table[(st,end)]
    max_p = max(max_p,profit)
print(max_p)
