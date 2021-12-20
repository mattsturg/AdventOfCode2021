from typing import List

def numberIncreases(depthMeasurments: List) -> int:
    count = 0
    first = True
    for depth in depthMeasurments:
        if not first and depth > lastDepth:
            count += 1
        if first:
            first = False
        lastDepth = depth
    return count

def compareGroups(depthMeasurments: List) -> int:
    count = 0
    groupA = 0
    groupB = 0
    backThree = -1
    backTwo = -1
    backOne = -1
    for depth in depthMeasurments:
        if backTwo > 0:
            groupA = depth + backOne + backTwo
        if backThree > 0:
            groupB = backOne + backTwo + backThree
            if groupA > groupB:
                count += 1
        backThree = backTwo
        backTwo = backOne
        backOne = depth
    return count

    return 0