# ip : consider yr has 360 days month 30 days and weeks has 6 days
# given total no of days print the yrs mon and weeks and days
days = int(input())
yrs = days//360
days %= 360
mon = days//30
days %= 30
weeks =days//6
days%= 6
print(f"{yrs} yrs {mon} mon {weeks} weeks {days} days" )