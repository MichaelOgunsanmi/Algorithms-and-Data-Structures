def rowMajorMethodDiagonalToSingle(diagonalMatrix):
    output = []
    i = 0

    while i < len(diagonalMatrix):
        j = 0
        while i >= j:
            output.append(diagonalMatrix[i][j])
            j += 1
        i += 1
    
    return output

answer = rowMajorMethodDiagonalToSingle(
[
[1,0,0,0], 
[1,9,0,0], 
[4,7,5,0], 
[1,12,8,6]
])

def rowMajorMethodSingleToDiagonal(singleMatrix):
    def getMatrixSize(singleMatrix):
        n = 0
        while singleMatrix != []:
            singleMatrix = singleMatrix[n:]
            n += 1         
        return n-1
    matrixSize = getMatrixSize(singleMatrix)
    output = [[0] * matrixSize for i in range(matrixSize)]

    i=0
    while i < matrixSize:
        j = 0
        while i >= j:
            output[i][j] = singleMatrix[int(((i*(i+1))/2) + j)]
            j += 1
        i += 1
    print(output)
    


rowMajorMethodSingleToDiagonal(answer)