# 7854
# prime digits in given number

prime_digits = 0
num = input()
for dig in num:
    if dig in "2357":
        prime_digits+=1
print(prime_digits)