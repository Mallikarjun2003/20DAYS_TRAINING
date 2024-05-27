from datetime import datetime

num = int(input())
current_dateTime = datetime.now()
print(current_dateTime)
while 1:
    flag = 0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            flag = 1
    if not flag:
        print(num)
        break
    num+=1
current_dateTime = datetime.now()

print(current_dateTime)
