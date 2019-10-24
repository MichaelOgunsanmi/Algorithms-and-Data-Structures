def transformToSparseMatrix(normalMatrix):
    rows = len(normalMatrix)
    columns = len(normalMatrix[0])
    output = []
    output.append([rows,columns])

    for row in range(rows):
        for column in range(columns):
            if normalMatrix[row][column] != 0:
                output.append([row + 1,column + 1,normalMatrix[row][column]])

    output[0].append(len(output) - 1)
    return output


# print(transformToSparseMatrix([
# [1,0,0,0,0], 
# [0,9,0,1,0], 
# [0,0,0,0,0], 
# [0,0,0,6,0]
# ]))

def addTwoSparseMatrices(firstSparseMatrix, secondSparseMatrix):
    firstMatrix = transformToSparseMatrix(firstSparseMatrix)
    secondMatrix = transformToSparseMatrix(secondSparseMatrix)
    output = []

    if firstMatrix[0][0] != secondMatrix[0][0] or firstMatrix[0][1] != secondMatrix[0][1]:
        return

    output.append([len(firstSparseMatrix), len(firstSparseMatrix[0])])
    firstIterator = 1
    secondIterator = 1
    while firstIterator < len(firstMatrix) and secondIterator < len(secondMatrix):
        if firstMatrix[firstIterator][0] > secondMatrix[secondIterator][0]:
            output.append(secondMatrix[secondIterator])
            secondIterator += 1
        elif firstMatrix[firstIterator][0] < secondMatrix[secondIterator][0]:
            output.append(firstMatrix[firstIterator])
            firstIterator += 1
        else:
            if firstMatrix[firstIterator][1] > secondMatrix[secondIterator][1]:
                output.append(secondMatrix[secondIterator])
                secondIterator += 1
            elif firstMatrix[firstIterator][1] < secondMatrix[secondIterator][1]:
                output.append(firstMatrix[firstIterator])
                firstIterator += 1
            else:
                output.append([firstMatrix[firstIterator][0], firstMatrix[firstIterator][1], firstMatrix[firstIterator][2] + secondMatrix[secondIterator][2]])
                firstIterator += 1
                secondIterator += 1
    
    if firstIterator < len(firstMatrix):
        for i in range(firstIterator, len(firstMatrix)):
            output.append(firstMatrix[i])
    elif secondIterator < len(secondMatrix):
        for i in range(secondIterator, len(secondMatrix)):
            output.append(secondMatrix[i])

    output[0].append(len(output) - 1)
    
    return output


# print(addTwoSparseMatrices([
# [0,0,3,0,0], 
# [4,0,0,0,7], 
# [0,0,5,0,8], 
# [0,6,0,6,0]
# ], [
# [1,0,0,0,0], 
# [0,9,0,1,0], 
# [0,0,0,0,0], 
# [0,0,0,6,0]
# ]))

# print(addTwoSparseMatrices([
# [2,0,0,0,0], 
# [2,0,0,0,0], 
# [2,0,0,0,0], 
# [2,0,0,0,0]
# ], [
# [1,1,1,1,1], 
# [0,0,0,0,0], 
# [0,0,0,0,0], 
# [0,0,0,0,0]
# ]))

def transformToNormalMatrix(sparseMatrix):
    rows = sparseMatrix[0][0]
    columns = sparseMatrix[0][1]

    output = [[0] * columns for i in range(rows)]

    for i in range(1, sparseMatrix[0][2] + 1):
        output[sparseMatrix[i][0] - 1][sparseMatrix[i][1] - 1] = sparseMatrix[i][2]

    return output

# print(transformToNormalMatrix (addTwoSparseMatrices([
# [2,0,0,0,0], 
# [2,5,0,0,0], 
# [2,0,0,0,0], 
# [2,0,0,0,6]
# ], [
# [1,1,1,1,1], 
# [0,2,0,0,0], 
# [0,0,0,0,0], 
# [0,0,0,0,0]
# ])))



