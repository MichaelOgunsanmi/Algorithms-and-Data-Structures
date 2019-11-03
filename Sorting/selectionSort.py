def selectionSort(arrayInput):  # Smarter implementation
    for i in range(len(arrayInput)):
        smallest = arrayInput[i]
        for j in range(i + 1, len(arrayInput)):
            if arrayInput[j] <= smallest:
                smallest = arrayInput[j]
                arrayInput[j], arrayInput[i] = arrayInput[i], smallest
    return arrayInput


# def selectionSort(arrayInput): #Out of the box(By definition implementation)
#     for i in range(len(arrayInput)):
#         for j in range(i + 1,len(arrayInput)):
#             if arrayInput[j] <= arrayInput[i]:               
#                 arrayInput[j], arrayInput[i] = arrayInput[i], arrayInput[j]
#                 print(arrayInput)
#     return arrayInput

arrayInput = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(selectionSort(arrayInput))

# Find the smallest element and swap it with the element in the first index
# Go again and find the next smallest index and swap with element in the second index.
# Contnue with find and swap until array is sorted
