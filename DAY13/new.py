# Please solve this question. Monica is making N food items for Joey. 
# Each of these food items has some nutritional value stored in an array V. 
# Help Monica to divide these food items into separate meals while making sure of the following points:

# Each meal should contain at least K number of food items.
# The difference between the maximum and the minimum nutritional value of food items in the meals should be at most M.
# Your task is to find and return the minimum number of meals in which Monica can divide the food items.
# If the food items cannot be divided into meals by following the above criteria, return -1.
# Input Specification:

#    Input 1: An integer value N, representing the number of food items.
#    Input 2: An integer value M, representing the maximum allowed nutritional value in a meal.
#    Input 3: An integer value K, representing the minimum number of food items required in one meal.
#    Input 4: An integer array V, representing the nutritional values of food items.
# Output Specification:

# Return the minimum number of meals in which Monica can divide the food items.
# Example 1:

#  Input 1: 3
#  Input 2: 1
#  Input 3: 1
#  Input 4: { 1, 1, 1 }
#  Output: 1
# Explanation:

# Here all 3 food items can be a single meal as 
# the difference between the maximum and minimum nutritional value of items is 0 
# while the maximum allowed difference is M = 1.

# Hence, 1 is returned as output.
# Example 2:

# Input 1: 2
# Input 2: 1
# Input 3: 2
# Input 4: { 1,4 }
# Output: -1
# Explanation:

# Here, we must put both items in one meal as 
# the number of food items is 2 and 
# the difference between the maximum and minimum allowed difference, M = 1.
# Hence, it is not possible to create a meal, so -1 is returned as output.
import heapq
n = int(input())
max_allowed_diff = int(input())
min_req = int(input())
arr = list(map(int,input().split()))
mini_heap = []
heapq.heapify(mini_heap)
arr.sort()
curr_meals = 0
visited = [False]*n
for i in range(n):
    mini_heap = []
    heapq.heapify(mini_heap)

    for j in range(n):
        if not visited[j]:
            if not mini_heap or arr[j] -mini_heap[0] <= max_allowed_diff:
                heapq.heappush(mini_heap, arr[j])
                visited[j]= True
    if len(mini_heap) >=min_req:
        curr_meals +=1
print(curr_meals) if curr_meals else print(-1)