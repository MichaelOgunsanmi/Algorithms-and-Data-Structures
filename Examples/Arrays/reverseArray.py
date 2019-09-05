def reverseArray(arrayInput):
        i = 0
        j = len(arrayInput) - 1

        while i <= j:
                arrayInput[i], arrayInput[j] = arrayInput[j], arrayInput[i]
                i += 1
                j -= 1

inputArr = [2,3,4,5,6,7, 8]
print(inputArr)
reverseArray(inputArr)
print(inputArr)