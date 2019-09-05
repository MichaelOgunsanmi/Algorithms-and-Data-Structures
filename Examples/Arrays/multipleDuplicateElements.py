def multipleDuplicateElements(arrayInput):
    duplicates = []
    lastDuplicate = float('-inf')
    for index in range(len(arrayInput) -1):
        if arrayInput[index] == arrayInput[index + 1] and arrayInput[index] != lastDuplicate:
            duplicates.append(arrayInput[index])
            lastDuplicate = arrayInput[index] 

    return duplicates 

def countMultipleDuplicates(arrayInput):
    hashTable = {}
    result = {}

    for element in arrayInput:
        hashTable[element] = hashTable.get(element, 0) + 1 
    
    for element in hashTable:
        value = hashTable[element]
        if value > 1:
            result[element] = value
    return result


print(multipleDuplicateElements([2,2,3,3,4,5,6,7,8,8,8,8,10,10,12,12]))
print(countMultipleDuplicates([8,3,6,4,6,5,6,8,2,7]))
