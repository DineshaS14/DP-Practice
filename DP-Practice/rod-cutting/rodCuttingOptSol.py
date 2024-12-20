# This function solves the rod-cutting problem using dynamic programming.
# It calculates the maximum revenue obtainable for a rod of length `n` given a price list `priceList`.
# Additionally, it provides the optimal solution, i.e., the lengths of pieces to cut to achieve the maximum revenue.

def rodCuttingWithOptimalSolution(priceList, rodLength):
    # dp[i] stores the maximum revenue obtainable for a rod of length i
    dp = [0] * (rodLength + 1)
    # cuts[i] stores the first cut length for a rod of length i to achieve maximum revenue
    cuts = [0] * (rodLength + 1)
    
    # Fill the dp array iteratively
    for currentLength in range(1, rodLength + 1):
        maxRevenue = float('-inf')
        # Try all possible first cut lengths
        for cutLength in range(1, currentLength + 1):
            # Calculate the revenue for making a cut at `cutLength`
            if cutLength <= len(priceList) - 1 and maxRevenue < priceList[cutLength] + dp[currentLength - cutLength]:
                maxRevenue = priceList[cutLength] + dp[currentLength - cutLength]
                cuts[currentLength] = cutLength  # Record the best cut length for current rod length
        dp[currentLength] = maxRevenue  # Update dp for current rod length
    
    # Reconstruct the solution (optimal cuts)
    solution = []
    while rodLength > 0:
        solution.append(cuts[rodLength])  # Add the first cut for the current rod length
        rodLength -= cuts[rodLength]  # Reduce the rod length by the length of the cut
    
    # Return the maximum revenue and the sequence of cuts
    return dp[-1], solution

# Test case for the function
if __name__ == "__main__":
    # Price list where priceList[i] is the price of a rod of length i
    # Length 0 is dummy for easier indexing
    priceList = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    rodLength = 8  # Length of the rod to be cut

    # Run the function
    maxRevenue, optimalCuts = rodCuttingWithOptimalSolution(priceList, rodLength)
    
    # Output the result
    print(f"Maximum Revenue: {maxRevenue}")
    print(f"Optimal Cuts: {optimalCuts}")
