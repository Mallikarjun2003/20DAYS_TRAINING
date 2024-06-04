# 4
# ____a____
# ___aba___
# __abcba__
# _abcdcba_
letters ='abcdefghijklmnopqrstuvwxyz'
num = int(input())
for i in range(1,num+1):
    print("_"*(num-i+1),end="")
    print(letters[:i-1]+letters[:i][::-1],end="")
    print("_"*(num-i+1),end="")
    print()


