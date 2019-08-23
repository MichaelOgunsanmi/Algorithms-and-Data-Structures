import math

def getDigit(number, placeValue):
    return math.floor(abs(number) / pow(10, placeValue)) % 10

def digitCount(number):
    if number == 0: return 1
    return math.floor(math.log10(abs(number))) + 1

def mostDigits(arrayInput):
    maxDigits = 0
    for number in arrayInput:
        maxDigits = max(maxDigits, digitCount(number))
    return maxDigits

def radixSort(arrayInput):
    maxDigitCount = int(mostDigits(arrayInput))

    for iteration in range(maxDigitCount):
        digitsBucket = [[] for i in range(10)]
        
        for index in range(len(arrayInput)):
            digit = int(getDigit(arrayInput[index], iteration))
            digitsBucket[digit].append(arrayInput[index])

        output = []
        for listElement in digitsBucket:
            if type(listElement) == int:
                output.append(listElement)
            else:
                output.extend(listElement)

        arrayInput = output        
    
    return arrayInput

    
print(radixSort([99,44,6,2,421,5,63,8447,283,4,0]))
# a  = [1,2,3,4,5, [6,7]]
# output = []
# for i in a:
#     if type(i) == int:
#         output.append(i)
#     else:
#         output.extend(i)

# for i in output:
