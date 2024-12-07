def greedyActivitySelector(startTimes, finishTimes):
    n = len(startTimes)
    selected = [0] # Always selecting the first activity on the list
    last = 0 #  keeps track of the index of the most recently selected activity

    for i in range(1, n):
        # Check if the start time of activity i is greater than or equal to
        # the finish time of the last selected activity
        if startTimes[i] >= finishTimes[last]:
            selected.append(i)
            last = i # update this for the next iteration
    return selected

# Test
startTimes = [1, 3, 0, 5, 3, 5, 6, 7, 8, 2, 12]
finishTimes = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
selected = greedyActivitySelector(startTimes, finishTimes)
print("Selected activities:", selected)
    
