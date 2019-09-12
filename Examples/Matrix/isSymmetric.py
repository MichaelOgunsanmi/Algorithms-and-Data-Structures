def isSymmetric(diagonalMatrix):
    i = 0
    j = 0
    while i < len(diagonalMatrix):
        while j < len(diagonalMatrix):
            if diagonalMatrix[i][j] != diagonalMatrix[j][i]:
                return False  
            j += 1
        i += 1
    return True 

print(isSymmetric(
[[1,0,0,0], 
[0,9,0,0], 
[0,0,5,0], 
[0,0,0,6]
]))
