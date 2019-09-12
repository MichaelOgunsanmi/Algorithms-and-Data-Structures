def convertDiagonalToSingleMatrix(diagonalMatrix):
    matrixSize = len(diagonalMatrix)
    output = []

    for index in range(matrixSize):
        output.append(diagonalMatrix[0][index])

    for index in range(1,matrixSize):
        output.append(diagonalMatrix[index][0])  

    return output

answer = convertDiagonalToSingleMatrix(
[
[2,3,4,5,6], 
[7,2,3,4,5], 
[8,7,2,3,4], 
[9,8,7,2,3],
[10,9,8,7,2]
])

print(answer)

def convertSingleToDiagonalMatrix(singleMatrix):
    matrixSize = int((len(singleMatrix) + 1 ) / 2)
    output = [[0] * matrixSize for i in range(matrixSize)]

    i = 0
    while i < matrixSize:
        j = 0
        while j < matrixSize:
            if i <= j:
                output[i][j] = singleMatrix[j-i]
            else:
                output[i][j] = singleMatrix[matrixSize - 1 + i -j]        
            j += 1
        i += 1

    return output

print(convertSingleToDiagonalMatrix(answer))