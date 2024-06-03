s =input()
stack =[]
for i in s:
    if stack and i =="*":
        stack.pop()
    elif i!="*":
        stack.append(i)
print("".join(stack))