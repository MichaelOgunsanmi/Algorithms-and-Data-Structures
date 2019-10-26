class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.head = None
        self.next = None


def convertPolynomialToLinkedList(polynomial):
    if polynomial == None:
        return

    output = None
    
    for i in range(len(polynomial)):
        newNode = Node(polynomial[i][0], polynomial[i][1])
        
        currentNode = output
        if currentNode == None:
            output = newNode
            output.head = newNode
        else:
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = newNode

    return output

polynomialLinkedList = convertPolynomialToLinkedList([[6,4], [5,3], [9,2], [2,1], [3,0]])

h = convertPolynomialToLinkedList([])

print(h)



def convertPolynomialToNumber(polynomialList, value):
    if polynomialList == None:
        return

    totalValue = 0
    currentNode = polynomialList.head

    while currentNode != None:
        totalValue += currentNode.coefficient * pow(value, currentNode.exponent)
        print(currentNode.coefficient, pow(value, currentNode.exponent))
        print()
        print(totalValue)
        currentNode = currentNode.next

    return totalValue


# print(convertPolynomialToNumber(polynomialLinkedList,120))

def convertLinkedListToPolynomial(linkedList):
    if linkedList == None:
        return

    output = []

    currentNode = linkedList.head

    while currentNode != None:
        output.append([linkedList.coefficient, linkedList.exponent])
        currentNode = currentNode.next 

    return output

def addTwoPolynomials(firstPolynomial, secondPolynomial):
    firstList = convertPolynomialToLinkedList(firstPolynomial)
    secondList = convertPolynomialToLinkedList(secondPolynomial)

    if firstList == None or secondList == None:
        if firstList == None and secondList == None:
            return None

        output = firstList if secondList == None else secondList
        return convertLinkedListToPolynomial(output)

    firstIterator = firstList.head
    secondIterator = secondList.head
    output = []

    while firstIterator != None and secondIterator != None:
        if firstIterator.exponent > secondIterator.exponent:
            output.append([firstIterator.coefficient, firstIterator.exponent])
            firstIterator = firstIterator.next
        elif firstIterator.exponent < secondIterator.exponent:
            output.append([secondIterator.coefficient, secondIterator.exponent])
            secondIterator = secondIterator.next
        else:
            output.append([firstIterator.coefficient + secondIterator.coefficient, firstIterator.exponent])
            firstIterator = firstIterator.next
            secondIterator = secondIterator.next

    currentNode = firstIterator if firstIterator != None else secondIterator

    while currentNode != None:
        output.append([currentNode.coefficient, currentNode.exponent])
        currentNode = currentNode.next
    
    return output




print(addTwoPolynomials([[6,4], [5,3], [9,2], [2,1], [3,0]], [[6,6], [2,5], [5,4], [2,1]]))