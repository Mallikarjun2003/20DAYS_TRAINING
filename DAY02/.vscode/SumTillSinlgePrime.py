#537 sum of digits = 6 not prime so ... 538 sod 7 single digit prime so .. print 538
num = int(input())
temp = num
primes = set([2,3,5,7])
while num < 10:
    if num in primes:
          print(num)
          break
    num+=1
        
while num>=10:
    found = 0
    sum = 0
    while num:
        sum += num%10
        num//=10
    if sum<10:
        if sum in primes:
            print(temp)
            found = 1
            break
    else:
            num =sum
    if num <= 10:
            num = temp+1
            temp = num
    if found:
        break
        

