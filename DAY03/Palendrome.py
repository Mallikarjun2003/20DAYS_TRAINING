def palindrome(num, rev):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return palindrome(num // 10, rev)

num = int(input("Enter a number: "))
reverse = 0
rev = palindrome(num, reverse)
print(f"Is {num} a palindrome? {num == rev}")
