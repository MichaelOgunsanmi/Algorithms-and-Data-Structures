def insertionSort(arrayInput):
    for i in range(1, len(arrayInput)):
        key = arrayInput[i]
        j = i - 1
        while j>= 0 and key < arrayInput[j]:
            arrayInput[j+1] = arrayInput[j]
            j -= 1      
        arrayInput[j+1] = key
    
    return arrayInput

arrayInput = [99,44,6,2,1,5,63,87,283,4,0]

print(insertionSort(arrayInput))


# Assume the first element is sorted. 
# Take the second element and determine where to place it in the list of already sorted data
# Continue with this approach for every other element until you completely sort the array.
# Given [5,4,3] => [5,5,3] => [4,5,3] => [4,5,5] => [4,4,5] => [3,4,5]