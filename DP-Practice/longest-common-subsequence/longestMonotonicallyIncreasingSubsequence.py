'''
Give an O.n lg n/-time algorithm to ûnd the longest monotonically increasing sub-
sequence of a sequence of n numbers. (Hint: The last element of a candidate subse-
quence of length i is at least as large as the last element of a candidate subsequence
of length i  1. Maintain candidate subsequences by linking them through the input
sequence.
'''
from bisect import bisect_left

def longestIncreasingSubsequenceOptimized(nums):
    """
    Find the length of the longest increasing subsequence in a given list of numbers.
    This function uses a greedy approach with binary search for optimization.

    :param nums: List of integers
    :return: Length of the longest increasing subsequence
    """
    # List to store the smallest ending element of all increasing subsequences of different lengths
    sub = []  

    # Iterate through each number in the input list
    for num in nums:
        # Find the position where 'num' can be placed in 'sub' to maintain sorted order
        # Using binary search for efficiency (O(log n) operation)
        pos = bisect_left(sub, num)

        if pos == len(sub):
            # If 'num' is greater than all elements in 'sub', it extends the longest subsequence
            sub.append(num)
        else:
            # Otherwise, replace the element at index 'pos' with 'num'
            # This ensures 'sub' contains the smallest possible elements for each subsequence length
            sub[pos] = num

    # The length of 'sub' represents the length of the longest increasing subsequence
    return len(sub)

# Test case to demonstrate the functionality
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longestIncreasingSubsequenceOptimized(nums))  # Output: 4
