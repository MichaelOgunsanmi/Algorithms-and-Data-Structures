def mergeSort(arrayInput):
    if len(arrayInput) == 1:
        return arrayInput
    
    #SPLIT ARRAY 
    middle = len(arrayInput)/2
    leftArray = arrayInput[:middle]
    rightArray = arrayInput[middle:]

    return merge(mergeSort(leftArray), mergeSort(rightArray))

def merge(leftArray, rightArray):
    result = []
    leftArrayIndex = 0
    rightArrayIndex = 0

    while leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray):
        leftArrayElement = leftArray[leftArrayIndex]
        rightArrayElement = rightArray[rightArrayIndex]
        if leftArrayElement <= rightArrayElement:
            result.append(leftArrayElement)
            leftArrayIndex += 1
        else:
            result.append(rightArrayElement)
            rightArrayIndex += 1 

    return result + leftArray[leftArrayIndex:] + rightArray[rightArrayIndex:]

print(mergeSort([99,44,6,2,1,5,63,87,283,4,0]))


