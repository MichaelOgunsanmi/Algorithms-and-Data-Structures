def countSort(arrayInput):
    maximumElement = max(arrayInput)
    newArray = [0] * (maximumElement + 1)

    for element in arrayInput:
        newArray[element] += 1

    arrayInputIndex = 0
    newArrayIndex = 0

    while newArrayIndex < len(newArray):
        if newArray[newArrayIndex] > 0:
            arrayInput[arrayInputIndex] = newArrayIndex
            arrayInputIndex += 1
            newArray[newArrayIndex] -= 1
        else:
            newArrayIndex += 1

    return arrayInput


print(countSort([99, 44, 44, 2, 1, 5, 63, 87, 283, 4, 0]))

# Get the maximum element
# Create a new array the size of the maximum element
# loop through the input array and update the count of the newArray created by
# 1 whenever a value is reached in the input array at the index of the created
# array similar to the value in the new array e.g if you see 77 in the input array,
# go to index 77 in the created array and increase its value by 1
# lastly, loop through the created array and read the count value for each index,
# then write the value in the input array, depending on the count times
