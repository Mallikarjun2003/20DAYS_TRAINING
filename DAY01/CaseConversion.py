# placements
# replace all the consonants in lowercase and vowels in upper
s = input().lower()
vowels =set(list("aeiou"))
for i in range(len(s)):
    if s[i] in vowels:
        s = s[:i]+"s[i].upper()"+s[i+1:]
print(s)