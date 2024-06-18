from collections import defaultdict
arr = [4, 4, 4,4 ]
freq = defaultdict(int)
n = len(arr)
for i in arr:
    freq[i] += 1
operations = 0
for idx,ele in enumerate(arr):
    if freq[ele] > 1:
        missing = 0
        for i in range(1,n+1):
            if not freq[i]:
                missing = i
                break
        if missing:
            freq[ele]-=1
            freq[missing] +=1
        arr[idx] = missing
        operations += abs(ele - missing)
print(arr)
print(operations)


# from collections import defaultdict

# def transform_array(arr):
#     n = len(arr)
#     freq = defaultdict(int)
    
#     # Count the frequency of each element in the array
#     for num in arr:
#         freq[num] += 1
    
#     # Track the missing numbers from 1 to n
#     missing = [i for i in range(1, n+1) if freq[i] == 0]
#     missing_idx = 0

#     # Perform the transformation
#     for i in range(n):
#         if freq[arr[i]] > 1:
#             freq[arr[i]] -= 1
#             arr[i] = missing[missing_idx]
#             freq[missing[missing_idx]] += 1
#             missing_idx += 1
    
#     return arr

# # Test the function with the example given in the problem
# arr = [4, 4, 4, 4]
# result = transform_array(arr)
# print(result)

    
