def middleElement(linkedList):
    fastPointer = linkedList.head
    slowPointer = linkedList.head

    while fastPointer != linkedList.tail and fastPointer.next != linkedList.tail:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next

    if fastPointer == linkedList.last:
        print(slowPointer.value)
    else:
        print(slowPointer.value, slowPointer.next.value)
    
def midElem(linkedList): #without using the tail attribute
    fastPointer = linkedList.head
    slowPointer = linkedList.head

    if fastPointer.next != None and fastPointer.next.next != None:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next 

    if fastPointer.next == None:
        print(slowPointer.value)
    else:
        print(slowPointer.value, slowPointer.next.value)