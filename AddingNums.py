nums = input().split()
floats = 0
odd_sum = even_sum = 0
for num in nums:
    if "." in num:
        floats += float(num)
    else:
        num = int(num)
        if num%2:
            odd_sum+=num
        else:
            even_sum+=num
print(floats , odd_sum , even_sum)

