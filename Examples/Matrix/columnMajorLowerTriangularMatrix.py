def columnMajorMethodDiagonalToSingle(diagonalMatrix):
    output = []
    i = 0

    while i < len(diagonalMatrix):
        j = i
        while j < len(diagonalMatrix):
            output.append(diagonalMatrix[j][i])
            j += 1

        i += 1
    
    return output

answer = columnMajorMethodDiagonalToSingle(
[
[1,0,0,0], 
[1,9,0,0], 
[4,7,5,0], 
[1,12,8,6]
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
        j = 0
        while i >= j:
            k=0
            r=0
            while k < j:
                r+= matrixSize-k
                k+=1
            r+= i-j
            output[i][j] = singleMatrix[r]
            j += 1
        i += 1
    print(output)
    


columnMajorMethodSingleToDiagonal(answer)