def lcsLength(X, Y):
    """
    Compute the length of the Longest Common Subsequence (LCS) using Dynamic Programming.

    :param X: First sequence.
    :param Y: Second sequence.
    :return: The length of the LCS and the filled LCS table.
    """
    m, n = len(X), len(Y)
    # Create DP table for LCS lengths
    dpTable = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Characters match
                dpTable[i][j] = dpTable[i - 1][j - 1] + 1
            else:  # Characters do not match
                dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])

    return dpTable[m][n], dpTable


def reconstructLCS(X, Y, dpTable):
    """
    Reconstruct the Longest Common Subsequence (LCS) from the DP table.

    :param X: First sequence.
    :param Y: Second sequence.
    :param lcsTable: DP table containing LCS lengths.
    :return: The LCS as a string.
    """
    i, j = len(X), len(Y)
    lcs = []

    # Trace back through the table to reconstruct the LCS
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])  # Match found, add to LCS
            i -= 1
            j -= 1
        elif dpTable[i - 1][j] >= dpTable[i][j - 1]:
            i -= 1  # Move up in the table
        else:
            j -= 1  # Move left in the table

    return ''.join(reversed(lcs))


# Test Case
X = "ABCBDAB"
Y = "BDCABA"
length, table = lcsLength(X, Y)
lcs = reconstructLCS(X, Y, table)

print(f"Length of LCS: {length}")
print(f"LCS: {lcs}")
