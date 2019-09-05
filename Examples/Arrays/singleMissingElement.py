def singleMissingElement(arrayInput):
    standardDifference = arrayInput[0]

    leftIndex = 0
    rightIndex = len(arrayInput) - 1 

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2

        if arrayInput[middleIndex] - middleIndex  == standardDifference:
            leftIndex = middleIndex + 1
            if arrayInput[leftIndex] - leftIndex == standardDifference + 1:
                return arrayInput[middleIndex] + 1
        elif arrayInput[middleIndex-1] - ( middleIndex- 1) == standardDifference:
            return arrayInput[middleIndex] - 1
        else:
            rightIndex = middleIndex - 1 
        


print(singleMissingElement([0,1,2,3,4,5,6,7,8,9,10,12]))