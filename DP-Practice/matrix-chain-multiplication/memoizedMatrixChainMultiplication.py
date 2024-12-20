def memoizedMatrixChainMultiplication(dimensions, numMatrices):
    """
    Finds the minimum cost of multiplying a chain of matrices using a top-down memoization approach.

    :param dimensions: List of matrix dimensions.
    :param numMatrices: Number of matrices.
    :return: Minimum multiplication cost.
    """
    # create a func to store the min cost for subproblems, init to infinity
    # memoTaable = [[float('inf')] * (numMatrices + 1) for _ in range(numMatrices + 1)]
    # Step-by-step initialization
    memoTable = []  # Start with an empty list
    for _ in range(numMatrices + 1):  # Repeat numMatrices + 1 times
        row = [float('inf')] * (numMatrices + 1)  # Create a row with numMatrices + 1 elements, all set to infinity
        memoTable.append(row)  # Add the row to the table

    # Helper function to compute minimum cost recursively with memoization.
    def lookupChain(memoTable, dimensions, start, end):
        if memoTable[start][end] < float('inf'):  # If already computed, return the cached value.
            return memoTable[start][end]
        if start == end:  # Single matrix case, cost is 0.
            memoTable[start][end] = 0
        else:
            for splitPoint in range(start, end):
                # Compute cost for splitting at splitPoint.
                cost = (lookupChain(memoTable, dimensions, start, splitPoint) +
                        lookupChain(memoTable, dimensions, splitPoint + 1, end) +
                        dimensions[start - 1] * dimensions[splitPoint] * dimensions[end])
                # Store the minimum cost.
                memoTable[start][end] = min(memoTable[start][end], cost)
        return memoTable[start][end]

    return lookupChain(memoTable, dimensions, 1, numMatrices)
# Test Case
matrixDimensions = [10, 30, 5, 60]
numberOfMatrices = len(matrixDimensions) - 1
print("Minimum cost using memoized matrix chain:", memoizedMatrixChainMultiplication(matrixDimensions, numberOfMatrices))
