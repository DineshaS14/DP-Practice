'''
Give a memoized version of LC S-LENGTH that runs in O.mn/ time.
'''
def lcsMemoized(strX, strY):
    """
    Compute the length of the longest common subsequence (LCS) between two strings
    using memoization.
    
    :param strX: First string
    :param strY: Second string
    :return: Length of the LCS
    """
    m, n = len(strX), len(strY)
    memo = [[-1] * (n + 1) for _ in range(m + 1)]  # Initialize memoization table
    
    def lcsHelper(i, j):
        """
        Helper function to compute LCS using memoization.
        
        :param i: Current index in strX
        :param j: Current index in strY
        :return: Length of LCS for strX[:i] and strY[:j]
        """
        if i == 0 or j == 0:
            # Base case: If either string is empty, LCS is 0
            return 0
        if memo[i][j] != -1:
            # If already computed, return the stored value
            return memo[i][j]
        if strX[i - 1] == strY[j - 1]:
            # If last characters match, include them in the LCS
            memo[i][j] = 1 + lcsHelper(i - 1, j - 1)
        else:
            # Otherwise, consider two cases: exclude from strX or exclude from strY
            memo[i][j] = max(lcsHelper(i - 1, j), lcsHelper(i, j - 1))
        return memo[i][j]
    
    return lcsHelper(m, n)


# Test case
strX = "ABCBDAB"
strY = "BDCABA"
print(f"Length of LCS: {lcsMemoized(strX, strY)}")  # Output: 4
