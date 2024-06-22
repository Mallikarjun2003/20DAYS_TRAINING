# Question -:You are given a binary string B of length L which contains K ones and remaining zeros. You are required to place the K ones in the binary string in such a way that the longest consecutive zeros have the least length possible. Once such a binary string is constructed, you are required to print the length of the contiguous block of zeros, which has the largest length.

# Constraints
# 0 <= K <= L

# 1 <= L <= 10^6
 
# Input
# Single line consisting of two space separated integers denoting L and K.
# Output
# Print a single integer denoting the length of the longest consecutive zeros as per the problem.
 
# Time Limit (secs)
# 1
 
# Examples
 
# Example 1
# Input
# 3 1
# Output
# 1
# Explanation
# B is of length 3 and it has 1 one’s.
# So the possible strings as per the problem are 010, 001, 100.
# In the first case, the maximum length of consecutive zeros is 1 whereas in the other two cases it is 2. Hence the constructed binary string is 010 and the output is 1.
 
# Example 2
# Input
# 3 3
# Output
# 0
# Explanation
# B is of length 3 and it has all three one’s. There is no block of zeros, hence the output is 0.

# Function to calculate the length of the longest contiguous block of zeros
def longest_zero_block(L, K):
    if K == 0:
        return L  # No ones, all zeros
    if K >= L:
        return 0  # All ones or more ones than the length of the string
    
    # Total zeros
    total_zeros = L - K
    # Minimum number of zeros in each block
    min_zeros_per_block = total_zeros // (K + 1)
    # Extra zeros to distribute
    extra_zeros = total_zeros % (K + 1)
    
    # If there are extra zeros, they will be distributed to some blocks making them one zero longer
    if extra_zeros > 0:
        return min_zeros_per_block + 1
    else:
        return min_zeros_per_block

# Input reading
L, K = map(int, input().split())

# Output the length of the longest contiguous block of zeros
print(longest_zero_block(L, K))
