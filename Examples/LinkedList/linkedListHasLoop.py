def linkedListHasLoop(linkedList):
    slowPointer = linkedList.head
    fastPointer = linkedList.head

    while fastPointer != None and fastPointer.next != None:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

        if fastPointer == slowPointer:
            return True

    
    return False


def createLinkedListWithLoop():
    linkedList = SinglyLinkedlist()

    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(4)

    lastNode = linkedList.tail

    linkedList.append(5)
    linkedList.append(6)

    linkedList.tail.next = lastNode

    return linkedList


loopLinkedList = createLinkedListWithLoop()
print(linkedListHasLoop(loopLinkedList))