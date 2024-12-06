'''
Give an O.n 2 /-time algorithm to ûnd the longest monotonically increasing subse-
quence of a sequence of n numbers.
'''
def longestIncreasingSubsequence(nums):
    """
    Find the length of the longest increasing subsequence in a given list of numbers.
    This function uses a dynamic programming approach.

    :param nums: List of integers
    :return: Length of the longest increasing subsequence
    """
    # Number of elements in the input list
    n = len(nums)

    # Initialize a DP table where dp[i] represents the length of the LIS ending at index i
    dp = [1] * n  # Each element is initially its own subsequence of length 1

    # Iterate through the list, comparing each pair of elements
    for i in range(1, n):
        for j in range(i):
            # If nums[i] can extend the subsequence ending at nums[j], update dp[i]
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The maximum value in the dp table is the length of the LIS
    return max(dp) if nums else 0  # Handle edge case for empty list

# Test case to demonstrate the functionality
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longestIncreasingSubsequence(nums))  # Output: 4
