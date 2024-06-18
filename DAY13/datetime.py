time = input().split("-")
yr=mon =date = -1
res = [0]*3
for i in range(len(time)):
    if len(time[i]) == 4:
        res[i] = "YYYY"
    elif len(time[i]) == 3:
        res[i]= "MM"
print(res) 
else:
    time = list(map(int,time))
    month_count = 0
    month_idx , day_idx = -1,-1
    days = 0
    for idx,i in enumerate(time):
        if i <= 12:
            month_count +=1
            month_idx = idx
        elif i > 12:
            days+=1
            day_idx = idx
    if month_count >= 2:
        print(-1)
        

print(yr,mon,)
