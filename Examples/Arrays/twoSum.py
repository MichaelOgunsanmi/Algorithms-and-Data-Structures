def twoSum(arrayInput, key):
    hashTable = {}
    result = []

    for element in arrayInput:
        hashTable[element] = hashTable.get(element, 0) + 1
        
    for element in arrayInput:
        if (key - element) in hashTable:            
            hashTable[element] = hashTable[element] - 1 
            hashTable[key - element] = hashTable[key - element] - 1 
            if hashTable[element] >= 0 and hashTable[key - element] >= 0:
                pair = [element, key-element]
                result.append(pair)

    return result   

print(twoSum([6,3,8,10,16,7,5,2,9,14], 10))