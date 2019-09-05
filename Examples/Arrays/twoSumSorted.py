def twoSumSorted(arrayInput, key):
    result = []
    leftIndex = 0
    rightIndex = len(arrayInput) - 1

    while leftIndex < rightIndex:
        leftElement = arrayInput[leftIndex]
        rightElement = arrayInput[rightIndex]
 
        if leftElement + rightElement > key:
            rightIndex -= 1
        elif leftElement + rightElement < key:
            leftIndex += 1 
        else:
            result.append([leftElement, rightElement])
            leftIndex += 1
            rightIndex -= 1

    return result
        
print(twoSumSorted([1,3,4,5,6,8,9,10,12,14], 10))
