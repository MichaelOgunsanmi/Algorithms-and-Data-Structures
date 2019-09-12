def convertDiagonalToSingleMatrix(diagonalMatrix):
    matrixSize = len(diagonalMatrix)
    output = []

    for index in range(matrixSize):
        output.append(diagonalMatrix[index][index])

    return output

print(convertDiagonalToSingleMatrix(
[
[1,0,0,0], 
[0,9,0,0], 
[0,0,5,0], 
[0,0,0,6]
]))

def convertSingleToDiagonalMatrix(singleMatrix):
    matrixSize = len(singleMatrix)
    output = [[0] * matrixSize for i in range(matrixSize)]

    for i in range(matrixSize):
        output[i][i] = singleMatrix[i]

    return output

print(convertSingleToDiagonalMatrix([1,9,5,6]))