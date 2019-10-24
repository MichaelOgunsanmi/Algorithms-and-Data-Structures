def convertPolynomialToNumber(polynomial, value):
    totalValue = 0

    for i in range(len(polynomial)):
        totalValue += polynomial[i][0] * pow(value, polynomial[i][1])

    return totalValue


# print(convertPolynomialToNumber([[5,4], [2,2], [5,0]], 2))
# print(convertPolynomialToNumber([[6,4], [5,3], [9,2], [2,1], [3,0]], 2))

def addTwoPolynomials(firstPolynomial, secondPolynomial):
    output = []
    firstIterator = 0
    secondIterator = 0

    while firstIterator < len(firstPolynomial) and secondIterator < len(secondPolynomial):
        if firstPolynomial[firstIterator][1] > secondPolynomial[secondIterator][1]:
            output.append(firstPolynomial[firstIterator])
            firstIterator += 1
        elif secondPolynomial[secondIterator][1] > firstPolynomial[firstIterator][1]:
            output.append(secondPolynomial[secondIterator])
            secondIterator += 1
        else:
            output.append([firstPolynomial[firstIterator][0] + secondPolynomial[secondIterator][0] ,firstPolynomial[firstIterator][1]])
            firstIterator += 1
            secondIterator += 1


    if firstIterator < len(firstPolynomial):
        for i in range(firstIterator, len(firstPolynomial)):
            output.append(firstPolynomial[firstIterator])
    elif secondIterator < len(secondPolynomial):
        for i in range(secondIterator, len(secondPolynomial)):
            output.append(secondPolynomial[secondIterator])

    return output


print(addTwoPolynomials([[5,4], [2,2], [5,0]], [[6,4], [5,3], [9,2], [2,1], [3,0]]))
