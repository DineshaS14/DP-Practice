def matrixChainOrder(dimensions, numMatrices):
    """
    Finds the minimum cost of multiplying a chain of matrices using a bottom-up dynamic programming approach.

    :param dimensions: List of matrix dimensions.
    :param numMatrices: Number of matrices.
    :return: Minimum multiplication cost and split points.
    """
    # Initialize cost table and split table.
    costTable = [[0] * (numMatrices + 1) for _ in range(numMatrices + 1)]
    splitTable = [[0] * (numMatrices + 1) for _ in range(numMatrices + 1)]

    # Iterate over chain lengths from 2 to numMatrices.
    for chainLength in range(2, numMatrices + 1):
        for start in range(1, numMatrices - chainLength + 2):
            end = start + chainLength - 1
            costTable[start][end] = float('inf')  # Set initial cost to infinity.
            for splitPoint in range(start, end):  # Try all possible splits.
                # Compute cost for current split.
                cost = (costTable[start][splitPoint] +
                        costTable[splitPoint + 1][end] +
                        dimensions[start - 1] * dimensions[splitPoint] * dimensions[end])
                if cost < costTable[start][end]:  # Update minimum cost and split point.
                    costTable[start][end] = cost
                    splitTable[start][end] = splitPoint

    return costTable, splitTable

# Test Case
matrixDimensions = [10, 30, 5, 60]
numberOfMatrices = len(matrixDimensions) - 1
costTable, splitTable = matrixChainOrder(matrixDimensions, numberOfMatrices)
print("Minimum cost using bottom-up matrix chain:", costTable[1][numberOfMatrices])
