# kth max in the list
import heapq
nums = [345,234,2]

heapq.heapify(nums)
print(nums)
heapq.heappush(nums,342)
heapq.heappop()
print(nums)