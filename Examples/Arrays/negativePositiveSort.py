def sortNegativePositive(arrayInput):
    i = 0
    j = len(arrayInput) - 1

    while i <=j:
        while arrayInput[i] < 0:
            i += 1
        while arrayInput[j] >= 0:
            j -= 1 

        if i < j:
            arrayInput[j], arrayInput[i] = arrayInput[i], arrayInput[j]

inputArr = [2,-3,4,-5,6,-7,8]
print(inputArr)
sortNegativePositive(inputArr)
print(inputArr)