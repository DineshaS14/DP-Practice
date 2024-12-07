def printOptimalParenthesization(splitTable, start, end):
    """
    Helper function to print the optimal parenthesization of a matrix chain.

    :param splitTable: Table of split points.
    :param start: Start index.
    :param end: End index.
    """
    if start == end:
        print(f"A{start}", end="")
    else:
        print("(", end="")
        printOptimalParenthesization(splitTable, start, splitTable[start][end])  # Print left part.
        printOptimalParenthesization(splitTable, splitTable[start][end] + 1, end)  # Print right part.
        print(")", end="")

# Test Case
matrixDimensions = [10, 30, 5, 60]
numberOfMatrices = len(matrixDimensions) - 1
costTable, splitTable = matrixChainOrder(matrixDimensions, numberOfMatrices)
print("Optimal parenthesization:")
printOptimalParenthesization(splitTable, 1, numberOfMatrices)
print("\nMinimum cost:", costTable[1][numberOfMatrices])
