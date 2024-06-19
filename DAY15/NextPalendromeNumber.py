ip : 1212
op : 1221
while(1):
    num = int(input())
    if num!=-1:
        def notpal(n):
            return not str(n) == str(n)[::-1]
        while notpal(num):
            num+=1
        else:
            print(num)
    else:
        break



