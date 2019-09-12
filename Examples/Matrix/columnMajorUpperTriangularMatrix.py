def columnMajorMethodDiagonalToSingle(diagonalMatrix):
    output = []
    j = 0

    while j < len(diagonalMatrix):
        i = 0
        while i <= j and i < len(diagonalMatrix):
            output.append(diagonalMatrix[i][j])
            i += 1

        j += 1
    
    return output

answer = columnMajorMethodDiagonalToSingle(
[
[1,7,5,4], 
[0,9,8,3], 
[0,0,5,2], 
[0,0,0,6]
])
print(answer)

def columnMajorMethodSingleToDiagonal(singleMatrix):
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
        j = i
        while i <= j and j < matrixSize:
            output[i][j] = singleMatrix[int(((j*(j+1))/2) + i)]
            j += 1
        i += 1
    print(output)
    


columnMajorMethodSingleToDiagonal(answer)