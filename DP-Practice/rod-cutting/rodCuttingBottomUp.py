'''
Length: 1, 2, 3, 4,  5,  6,  7,  8,  9, 10
Price:  1, 5, 8, 9, 10, 17, 17, 20, 24, 30

Step 1: Initialize dp array:
dp = [0, 0, 0, 0, 0]

Step 2: Compute for j = 1:
dp[1] = max(1 + dp[0]) = 1
dp = [0, 1, 0, 0, 0]

Step 3: Compute for j = 2:
dp[2] = max(1 + dp[1], 5 + dp[0]) = 5
dp = [0, 1, 5, 0, 0]

Step 4: Compute for j = 3:
dp[3] = max(1 + dp[2], 5 + dp[1], 8 + dp[0]) = 8
dp = [0, 1, 5, 8, 0]

Step 5: Compute for j = 4:
dp[4] = max(1 + dp[3], 5 + dp[2], 8 + dp[1], 9 + dp[0]) = 10
dp = [0, 1, 5, 8, 10]

'''
def rodCuttingBottomUp(p, n):
    # dp[i] will store the maximum revenue for rod of length i
    # filling it up with all 0's
    dp = [0] * (n + 1)
    # solve the sub problems iteratively
    for j in range(1, n + 1): # for each rod length
        maxRevenue = float('-inf')
        for i in range(1, n + 1): # try every possible first cut
            maxRevenue = max(maxRevenue, p[i] + dp[j - i])
        dp[j] = maxRevenue # store the max in dp for length j
    return dp[n]

# Test
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Price table with 1-based indexing
n = 4  # Rod length

result = rodCuttingBottomUp(p, n)
print(f"Maximum revenue for rod of length {n}: {result}")
