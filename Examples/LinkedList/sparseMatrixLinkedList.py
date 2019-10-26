class Node:
    def __init__(self, columnIndex, value):
        self.value = value
        self.columnIndex = columnIndex
        self.next = None


def transformToSparseMatrix(normalMatrix):
    rows = len(normalMatrix)
    columns = len(normalMatrix[0])

    output = [None] * (rows + 1)
    output[rows] = columns #store value of columns as would be used in recreating normal matrix
    
    for row in range(rows):
        for column in range(columns):
            if normalMatrix[row][column] != 0:
                newNode = Node(column, normalMatrix[row][column])
                if output[row] == None:
                    output[row] = newNode
                else:
                    currentNode = output[row]
                    while currentNode.next != None:
                        currentNode = currentNode.next
                    
                    currentNode.next = newNode

    return output
                    




def transformToNormalMatrix(sparseMatrix):
    if sparseMatrix == None:
        return 

    rows = len(sparseMatrix) - 1
    output = [[0] * sparseMatrix[rows] for i in range(rows)]
    

    for row in range(rows):
        if sparseMatrix[row] != None:
            currentNode = sparseMatrix[row]
  
            while currentNode != None:
                output[row][currentNode.columnIndex] = currentNode.value
                currentNode = currentNode.next
        
    return output


# print( transformToNormalMatrix( transformToSparseMatrix([
# [1,0,0,0,0,8],
# [0,9,0,1,0,0], 
# [0,0,0,0,0,0], 
# [0,0,0,6,0,0],
# [0,0,0,0,9,0],
# [0,0,0,8,0,0],
# [0,0,7,0,0,0],
# [0,6,0,0,0,0]
# ])))


def addTwoSparseMatrices(firstSparseMatrix, secondSparseMatrix):
    firstMatrix = transformToSparseMatrix(firstSparseMatrix)
    secondMatrix = transformToSparseMatrix(secondSparseMatrix)
    

    if len(firstMatrix) != len(secondMatrix) or firstMatrix[len(firstMatrix) - 1] != secondMatrix[len(secondMatrix) - 1]:
        return

    output = [None] * len(firstMatrix)
    output[len(firstMatrix) - 1] = firstMatrix[len(firstMatrix) - 1]

    for row in range(len(firstMatrix) - 1):
        if firstMatrix[row] != None or secondMatrix[row] != None:
            firstIterator = firstMatrix[row]
            secondIterator = secondMatrix[row]

            while firstIterator != None and secondIterator != None:
                newNode = None
            
                if firstIterator.columnIndex < secondIterator.columnIndex:
                    newNode = Node(firstIterator.columnIndex, firstIterator.value)
                    firstIterator = firstIterator.next
                elif firstIterator.columnIndex > secondIterator.columnIndex:
                    newNode = Node(secondIterator.columnIndex, secondIterator.value)
                    secondIterator = secondIterator.next
                else:
                    newNode = Node(firstIterator.columnIndex, firstIterator.value + secondIterator.value)
                    firstIterator = firstIterator.next
                    secondIterator = secondIterator.next
  
                if output[row] == None:
                    output[row] = newNode
                else:
                    currentNode = output[row]

                    while currentNode.next != None:
                        currentNode = currentNode.next
                    
                    currentNode.next = newNode
   
            if firstIterator != None or secondIterator != None:
                if output[row] == None:
                    output[row] = firstIterator if firstIterator != None else secondIterator
                else:
                    currentNode = output[row]

                    while currentNode.next != None:
                        currentNode = currentNode.next
                    
                    currentNode.next = firstIterator if firstIterator != None else secondIterator
    return output


print(transformToNormalMatrix( addTwoSparseMatrices([
[2,2,2,2,2], 
[2,0,0,0,0], 
[2,0,0,0,0], 
[2,0,0,0,0]
], [
[1,1,1,1,1], 
[0,0,0,0,0], 
[0,0,0,0,0], 
[0,0,0,0,0]
])))