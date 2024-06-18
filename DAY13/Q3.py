from collections import defaultdict
n = int(input())
emails = defaultdict(int)
for _ in range(n):
    emails[input().split("@")[1]]+=1

email = list(emails.keys())
email.sort(key = lambda x:emails[x],reverse= True)

print(email)