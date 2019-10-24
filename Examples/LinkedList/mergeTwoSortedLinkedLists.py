def mergeTwoSortedLinkedLists(firstList, secondList):
    currentNode = None
    newHead = None
    firstCurrent = firstList.head
    secondCurrent = secondList.head 

    if firstCurrent.value < secondCurrent.value:
        currentNode = firstCurrent
        firstCurrent = firstCurrent.next
    else:
        currentNode = secondCurrent
        secondCurrent = secondCurrent.next
    
    currentNode.next = None
    newHead = currentNode

    while firstCurrent != None and secondCurrent != None:
            if firstCurrent.value < secondCurrent.value:
                currentNode.next = firstCurrent
                currentNode = firstCurrent
                firstCurrent = firstCurrent.next
            else:
                currentNode.next = secondCurrent
                currentNode = secondCurrent
                secondCurrent = secondCurrent.next

            currentNode.next = None

    if firstCurrent != None:
        currentNode.next = firstCurrent
    elif secondCurrent != None:
        currentNode.next = secondCurrent

    if newHead == firstList.head:
        firstList.printList()
    else:
        secondList.printList()



firstList = SinglyLinkedlist()
secondList = SinglyLinkedlist()
firstList.append(2)
firstList.append(4)
firstList.append(8)
firstList.append(12)
firstList.append(67)
firstList.append(77)
secondList.append(3)
secondList.append(17)
secondList.append(80)
mergeTwoSortedLinkedLists(firstList, secondList)