def singleDuplicateElement(arrayInput):
    standardDifference = arrayInput[0]

    leftIndex = 0
    rightIndex = len(arrayInput) - 1 

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2

        if arrayInput[middleIndex] - middleIndex  == standardDifference:
            leftIndex = middleIndex + 1
            if arrayInput[middleIndex] == arrayInput[leftIndex]:
                return arrayInput[middleIndex]
        elif arrayInput[middleIndex] == arrayInput[middleIndex-1]:
            return arrayInput[middleIndex]
        else:
            rightIndex = middleIndex - 1 
        


print(singleDuplicateElement([2,3,4,5,6,6,7,8,9]))