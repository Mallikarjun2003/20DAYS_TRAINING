def min_operations_to_permutation(arr):
    n = len(arr)
    freq = [0] * (n + 1)
    missing = []
    result = arr[:]
    for num in arr:
        if 1 <= num <= n:
            freq[num] += 1
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing.append(i)
    j = 0
    used = set()
    for i in range(n):
        if arr[i] in used or arr[i] > n or freq[arr[i]] > 1:
            if j < len(missing):
                if arr[i] <= n:
                    freq[arr[i]] -= 1
                result[i] = missing[j]
                j += 1
        else:
            used.add(arr[i])
    
    return result
arr = [4, 4, 3, 3]
print(min_operations_to_permutation(arr))
