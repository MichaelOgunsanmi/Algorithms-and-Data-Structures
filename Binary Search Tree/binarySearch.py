def binarySearch(arrayInput, key):
    leftIndex = 0
    rightIndex = len(arrayInput) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2

        if arrayInput[middleIndex] == key:
            return True
        elif key > arrayInput[middleIndex]:
            leftIndex = middleIndex + 1
        else:
            rightIndex = middleIndex - 1

    return False


print(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
