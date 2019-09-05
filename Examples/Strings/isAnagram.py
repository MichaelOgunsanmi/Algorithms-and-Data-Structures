def isAnagram(stringInput, compareString):
    if len(stringInput) != len(compareString):
        return False  
    hashTable = {}

    for alphabet in stringInput:
         hashTable[alphabet] = hashTable.get(alphabet, 0) + 1
    for alphabet in compareString:
        if alphabet not in hashTable:
            return False  
        else:
            hashTable[alphabet] = hashTable[alphabet] - 1
            if hashTable[alphabet] == 0:
                hashTable.pop(alphabet)

    return True  

print(isAnagram('decimal', 'medical'))