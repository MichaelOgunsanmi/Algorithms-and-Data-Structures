from LinkedLists.singlyLinkedList import SinglyLinkedList


def linkedListIntersection(firstList, secondList):
    currentNode = firstList.head
    firstStack = []

    while currentNode != None:
        firstStack.insert(0, currentNode.value)
        currentNode = currentNode.next

    currentNode = secondList.head
    secondStack = []

    while currentNode != None:
        secondStack.insert(0, currentNode.value)
        currentNode = currentNode.next

    pointOfIntersection = None

    while firstStack[0] == secondStack[0]:
        pointOfIntersection = firstStack.pop(0)
        secondStack.pop(0)
    
    return pointOfIntersection

firstList = SinglyLinkedList()
firstList.append(1)
firstList.append(2)
firstList.append(3)
firstList.append(4)
firstList.append(5)
firstList.append(6)


secondList = SinglyLinkedList()
secondList.append(9)
secondList.append(8)
secondList.append(7)
secondList.append(4)
secondList.append(5)
secondList.append(6)


print(linkedListIntersection(firstList, secondList))


