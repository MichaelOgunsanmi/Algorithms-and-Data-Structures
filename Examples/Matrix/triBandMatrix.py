def convertDiagonalToSingleMatrix(diagonalMatrix):
    matrixSize = len(diagonalMatrix)
    output = []

    for index in range(1, matrixSize):
        output.append(diagonalMatrix[index][index - 1])

    for index in range(matrixSize):
        output.append(diagonalMatrix[index][index])

    for index in range(matrixSize - 1):
        output.append(diagonalMatrix[index][index + 1])

    return output


answer = convertDiagonalToSingleMatrix(
    [
        [1, 4, 0, 0, 0],
        [4, 9, 4, 0, 0],
        [0, 3, 5, 2, 0],
        [0, 0, 3, 6, 7],
        [0, 0, 0, 6, 8]
    ])

print(answer)


def convertSingleToDiagonalMatrix(singleMatrix):
    def getMatrixSize(singleMatrix):
        n = 0
        while singleMatrix != []:
            singleMatrix = singleMatrix[n:]
            n += 1
        return n - 1

    matrixSize = getMatrixSize(singleMatrix)
    output = [[0] * matrixSize for i in range(matrixSize)]

    i = 0
    while i < matrixSize:
        j = 0
        while j < matrixSize:
            if i - j == 1:
                output[i][j] = singleMatrix[i - 1]
            elif i - j == 0:
                output[i][j] = singleMatrix[matrixSize - 1 + i]
            elif i - j == -1:
                output[i][j] = singleMatrix[(2 * matrixSize - 1) + j - 1]
            j += 1
        i += 1

    return output


print(convertSingleToDiagonalMatrix(answer))
