class Node:
    def __init__ (self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        self.length += 1

        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return
        
        newNode = Node(value)

        newNode.prev = self.tail
        self.tail.next = newNode

        self.tail = newNode
    
    def prepend(self, value):
        self.length += 1

        newNode = Node(value)

        self.head.prev = newNode
        newNode.next = self.head

        self.head = newNode

    def insert(self, value, index):
        if index >= self.length:
            self.append(value)
            return
        elif index == 0:
            self.prepend(value)
            return
        elif index < 0:
            print('Invalid index')
            return

        self.length += 1
        newNode = Node(value)

        leader = self.__traverseToIndex__(index - 1)
        restOfList = leader.next

        newNode.prev = leader
        leader.next = newNode

        restOfList.prev = newNode
        newNode.next = restOfList
    
    def removeValue(self, value):
        index = self.__traverseToValue__(value)

        if index == 0:
            newHead = self.head.next

            newHead.prev = None
            self.head.next = None

            self.head = newHead
            self.length -= 1
            return
        
        if index == -1:
            print('List does not contain "{value}"'.format(value = value))
            return

        
        leader = self.__traverseToIndex__(index - 1)
        unwantedNode = leader.next
        if index == self.length - 1:
            unwantedNode.prev = None
            leader.next = None

            self.tail = leader
            self.length -= 1
            return
        
        restOfList = leader.next.next

        restOfList.prev = leader
        leader.next = restOfList

        unwantedNode.prev = None
        unwantedNode.next = None
        self.length -= 1
    
    def deleteAtIndex(self, index):
        if not isinstance(index, int):
            print('Invalid index passed. Pass in a number')
            return
        if index == 0:
            newHead = self.head.next
            
            if newHead != None:
                newHead.prev = None
                self.head.next = None
            else:
                self.tail = None
            
            self.head = newHead
            self.length -= 1
            return
        if index < 0 or index >= self.length:
            print('Invalid index')
            return

        leader = self.__traverseToIndex__(index - 1)
        unwantedNode = leader.next

        if index == self.length - 1:
            unwantedNode.prev = None
            leader.next = None

            self.tail = leader 
            self.length -= 1
            return

        restOfList = leader.next.next

        restOfList.prev = leader
        leader.next = restOfList

        unwantedNode.prev = None
        unwantedNode.next = None

        self.length -= 1
    
    def len(self):
        currentNode = self.head
        length = 0
        while currentNode != None:
            length += 1
            currentNode = currentNode.next
        return length
    
    def reverse(self):
        if self.length <= 1:
            return self.head
        
        alreadyReversed = self.head
        self.tail = self.head
        currentNode = self.head.next
        alreadyReversed.prev = currentNode
        alreadyReversed.next = None

        while currentNode != None:
            storePointer = currentNode.next
            currentNode.prev = storePointer
            currentNode.next = alreadyReversed

            alreadyReversed = currentNode
            currentNode = storePointer
        
        self.head = alreadyReversed
        self.printList()
        
    def printList(self):
        currentNode = self.head
        linkedList = []

        while currentNode != None:
            linkedList.append(currentNode.value)
            currentNode = currentNode.next
        
        print(linkedList)

    def __traverseToIndex__(self, index):
        currentIndex = 0
        currentNode = self.head
        while currentIndex != index:
            currentIndex += 1
            currentNode = currentNode.next
        return currentNode

    def __traverseToValue__(self, value):
        currentIndex = 0
        currentNode = self.head
        currentValue = self.head.value
        while currentValue != value and currentIndex < self.length:
            currentIndex += 1
            if currentIndex == self.length:
                return -1
            currentNode = currentNode.next
            currentValue = currentNode.value
        return currentIndex


driver = DoublyLinkedList()
# driver.append(3)
# driver.append(4)
# driver.prepend(5)
# driver.prepend(7)
# driver.insert(99,2)
# driver.insert(2,2)
# driver.printList()
# driver.reverse()
# driver.removeValue(2)
# driver.printList() 
# print(driver.length)
# print(driver.len())
# driver.reverse()

# driver.append(1)
# driver.printList()
# driver.deleteAtIndex(0)
# driver.printList()

driver.append(1)
driver.append(2)
driver.append(3)
driver.printList()
driver.deleteAtIndex(2)
driver.printList()
