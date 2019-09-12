def rowMajorMethodDiagonalToSingle(diagonalMatrix):
    output = []
    i = 0

    while i < len(diagonalMatrix):
        j = i
        while j < len(diagonalMatrix):
            output.append(diagonalMatrix[i][j])
            j += 1
        i += 1
    
    return output

answer = rowMajorMethodDiagonalToSingle(
[
[1,4,3,2], 
[0,9,4,7], 
[0,0,5,8], 
[0,0,0,6]
])
print(answer)

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
        j = i
        while i <= j and j < matrixSize:
            k=0
            r=0
            while k < i:
                r+= matrixSize-k
                k+=1
            r+= j - i
            output[i][j] = singleMatrix[r]
            j += 1
        i += 1
    print(output)
    


rowMajorMethodSingleToDiagonal(answer)