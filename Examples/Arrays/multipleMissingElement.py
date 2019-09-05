def multipleMissingElement(arrayInput):
    missingElements = []
    for index in range(len(arrayInput) - 1):
        if arrayInput[index + 1] - arrayInput[index] > 1:
            numOfMissingElements = arrayInput[index + 1] - arrayInput[index] - 1

            if numOfMissingElements == 1:
                missingElements.append(arrayInput[index] + 1)
            else:
                for i in range(1,numOfMissingElements + 1):
                   missingElements.append(arrayInput[index] + i) 
    
    return missingElements 

def multipleMissingElementHash(arrayInput):
    missingElements = []
    hashTable = {}
    smallest = arrayInput[0]
    largest = arrayInput[0]
    

    for element in  arrayInput:
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element
        
        hashTable[element] = hashTable.get(element, 0)
    
    for index in range(smallest, largest+1):
        if index not in hashTable:
            missingElements.append(index)
    
    return missingElements

print(multipleMissingElementHash([20,16,3,12,24,8,23,10,6]))



