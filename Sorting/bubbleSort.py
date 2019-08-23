def bubbleSort(arrayInput):
    noSwaps = True
    for i in range(len(arrayInput) - 1):
        for j in range(len(arrayInput) - 1 - i): #with the i once sorted, it wont check that value again, saving on the number of swapping needed
            if arrayInput[j] > arrayInput[j + 1]:
                arrayInput[j], arrayInput[j+1] = arrayInput[j+1], arrayInput[j]
                noSwaps = False 
        if noSwaps: break  #Helps in the case the array is almost sorted
    return arrayInput



arrayInput = [9,8,7,6,5,4,3,2,1]

print(bubbleSort(arrayInput))


# Take the first and second element. Compare it and swap as appropriate.
# Contnue this compare ans swap until end of array 
# Go again and do compare and swap action until array is sorted.
# Once a number has been sorted, no need to compare it again, reason for len(arr) -1 - i