def quickSort(array, left, right):
    if left < right: #This helps to check if there is still  or more elements in the sub-array. If not, then the element is in its correct position in the whole array and no need to sort.
        pivot = right
        partitionIndex = partition(array, pivot, left, right)

        quickSort(array, left, partitionIndex - 1) #left array
        quickSort(array, partitionIndex + 1, right) #right array
    
    return array  

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left 

    index = left

    while index < right:
        if array[index] < pivotValue:
            swap(array, index, partitionIndex)
            partitionIndex += 1  #to get the index where we will swap our pivot value into
        index += 1
    
    swap(array, right, partitionIndex) #here we swp the pivot value and value at the point where the pivot value should correctly be
    return partitionIndex

def swap(array, firstIndex, secondIndex):
    array[firstIndex],array[secondIndex]  = array[secondIndex], array[firstIndex]
    

numbers = [99,44,6,2,1,5,63,87,283,4,0]
quickSort(numbers, 0, len(numbers) - 1)

print(numbers)