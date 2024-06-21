
from collections import defaultdict,deque
winners = defaultdict(int)
arr = deque(arr)
while arr:
    p1 , p2 = arr.popleft(),arr.popleft()
    if p1 > p2:
        winners[p1] +=1
        arr.appendleft(p1)
        arr.append(p2)
        if winners[p1] == k:
            print(p1)
            break
    else:
        winners[p2] +=1
        arr.appendleft(p2)
        arr.append(p1)
        if winners[p2] == k:
            print(p2)
            break

