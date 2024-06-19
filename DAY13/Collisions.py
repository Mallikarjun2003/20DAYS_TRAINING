n = int(input())
speeds = list(map(int,input().split()))

collisions = 0
pos = int(input())
for i in range(n):
    if i < pos:
        for j in range(i,pos):
            if speeds[j] > speeds[pos]:
                collisions += 1
    elif i > pos:
            for j in range(i,n):
                if speeds[j] < speeds[pos]:
                    collisions += 1
print(collisions)