def editDistance(strX, strY):
    """
    Calculate the edit distance between two strings and reconstruct the sequence of operations.
    :param strX: First string.
    :param strY: Second string.
    :return: Minimum edit distance and sequence of operations.
    """
    m, n = len(strX), len(strY)
    dpTable = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table
    for i in range(m + 1):
        dpTable[i][0] = i  # Deletion cost
    for j in range(n + 1):
        dpTable[0][j] = j  # Insertion cost

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if strX[i - 1] == strY[j - 1] else 1
            dpTable[i][j] = min(
                dpTable[i - 1][j] + 1,      # Deletion
                dpTable[i][j - 1] + 1,      # Insertion
                dpTable[i - 1][j - 1] + cost  # Substitution
            )

    # Backtrack to find the sequence of operations
    i, j = m, n
    operations = []
    while i > 0 or j > 0:
        if i > 0 and dpTable[i][j] == dpTable[i - 1][j] + 1:
            operations.append(f"Delete '{strX[i - 1]}' from X")
            i -= 1
        elif j > 0 and dpTable[i][j] == dpTable[i][j - 1] + 1:
            operations.append(f"Insert '{strY[j - 1]}' into X")
            j -= 1
        else:
            if strX[i - 1] != strY[j - 1]:
                operations.append(f"Substitute '{strX[i - 1]}' with '{strY[j - 1]}'")
            i -= 1
            j -= 1

    return dpTable[m][n], operations[::-1]  # Reverse operations for correct order


# Test case
x = "intention"
y = "execution"
distance, ops = editDistance(x, y)
print(f"Edit distance: {distance}")
print("Operations:")
for op in ops:
    print(op)
