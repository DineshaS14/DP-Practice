'''
Rod Cutting Recursion Tree (n = 4)

Level 1: rodCuttingRecursively(4)
    ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(3)
    │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(2)
    │      │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(1)
    │      │      │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(0)
    │      │      │      └── Base case: n = 0, Revenue = 0
    │      │      └── Max Revenue = 1 + 1 + 1 + 1 = 4
    │      │
    │      ├── Cut at 2: Revenue = p[2] + rodCuttingRecursively(1)
    │      │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(0)
    │      │      └── Max Revenue = 5 + 1 = 6
    │      │
    │      └── Cut at 3: Revenue = p[3] + rodCuttingRecursively(0)
    │             └── Max Revenue = 8
    │
    ├── Max Revenue for n = 3 = 8
    │
    ├── Cut at 2: Revenue = p[2] + rodCuttingRecursively(2)
    │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(1)
    │      │      └── Cut at 1: Revenue = p[1] + rodCuttingRecursively(0)
    │      │
    │      ├── Cut at 2: Revenue = p[2] + rodCuttingRecursively(0)
    │      └── Max Revenue = 5 + 5 = 10
    │
    ├── Cut at 3: Revenue = p[3] + rodCuttingRecursively(1)
    │      ├── Cut at 1: Revenue = p[1] + rodCuttingRecursively(0)
    │      └── Max Revenue = 8 + 1 = 9
    │
    ├── Cut at 4: Revenue = p[4] + rodCuttingRecursively(0)
    │      └── Base case: n = 0, Revenue = 9
    │
    └── Max Revenue for n = 4 = 10

'''
def rodCuttingRecursively(p, n):
    if n == 0:
        return 0
    maxRevenue = float('-inf')
    for i in range(1, n + 1):
        maxRevenue =  max(maxRevenue, p[i] + rodCuttingRecursively(p, n-i))
    return maxRevenue

# Price table (length -> price)
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Adding a 0 at the start for 1-based indexing
n = 4  # Length of the rod
# Test the function
max_revenue = rodCuttingRecursively(p, n)
print(f"The maximum revenue for a rod of length {n} is: {max_revenue}")
# The maximum revenue for a rod of length 4 is: 10

n = 7  # Length of the rod
max_revenue = rodCuttingRecursively(p, n)
print(f"The maximum revenue for a rod of length {n} is: {max_revenue}")
# The maximum revenue for a rod of length 7 is: 18
