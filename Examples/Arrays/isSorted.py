def isSorted(arrayInput):
    index = 0

    while index < len(arrayInput) - 1:
        if arrayInput[index] > arrayInput[index+1]:
            return False

        index += 1

    return True

print(isSorted([2,3,4,5,5,6,6,6,7]))