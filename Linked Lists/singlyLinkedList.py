class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedlist:
    def __init__(self):
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

        self.tail.next = newNode

        self.tail = newNode        

    def prepend(self, value):
        self.length += 1

        newNode = Node(value)

        newNode.next = self.head

        self.head = newNode

    def insert(self, value, index):
        if index >= self.length : #will be appended to the end
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

        leader.next = newNode
        newNode.next = restOfList

    def removeValue(self, value):       
        index = self.__traverseToValue__(value)
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        elif index == -1:
            print('List does not contain "{value}"'.format(value = value))
            return


        leader = self.__traverseToIndex__(index - 1)
        unwantedNode = leader.next

        leader.next = unwantedNode.next

        if index == self.length - 1 :
            self.tail = leader
            self.tail.next = None
        self.length -= 1
    
    def deleteAtIndex(self, index):
        if not isinstance(index, int):
            print('Invalid index passed. Pass in a number')
            return
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        elif index < 0 or index >= self.length:
            print('invalid index')
            return


        leader = self.__traverseToIndex__(index - 1)
        unwantedNode = leader.next

        leader.next = unwantedNode.next

        if index == self.length - 1 :
            self.tail = leader
            self.tail.next = None
        self.length -= 1

    def len(self):
        currentNode = self.head
        length = 0
        while currentNode != None:
            length += 1
            currentNode = currentNode.next
        return length
    
    def reverse(self):
        if self.length == 1:
            return self.head
        
        alreadyReversed = self.head
        self.tail = self.head
        currentNode = self.head.next
        alreadyReversed.next = None
        while currentNode != None:
            storePointer = currentNode.next
            currentNode.next = alreadyReversed

            alreadyReversed = currentNode
            currentNode = storePointer
        self.head = alreadyReversed
        
        self.printList()

    def reverseRecursive(self):
        listElements = []
        self.reverseLinkedListRecursive(self.head, self.head.next, listElements)
        print(listElements)

    def reverseLinkedListRecursive(self, currentNode, nextNode, listElements):
        if nextNode != None:
            self.reverseLinkedListRecursive(nextNode, nextNode.next, listElements)       
            nextNode.next = currentNode 
        else:
            
            self.head = currentNode
        
        listElements.append(currentNode.value)
        

    def printList(self):
        linkedList = []
        currentNode = self.head
        while currentNode != None:
            linkedList.append(currentNode.value)
            currentNode = currentNode.next
        print(linkedList)

    
    def printListReversedRecursive(self):
        listElements = []
        self.printListReversed(self.head, listElements)
        print(listElements)

    def printListReversed(self, currentNode, listElements):
        if currentNode == None:
            return
        
        self.printListReversed(currentNode.next, listElements)
        listElements.append(currentNode.value)

    
    def __traverseToIndex__(self, index):
        currentIndex = 0
        currentNode = self.head
        while currentIndex != index:
            currentIndex += 1
            currentNode = currentNode.next
        return  currentNode

    def __traverseToValue__(self, value):
        currentValue = self.head.value
        currentIndex = 0
        currentNode = self.head
        while currentValue != value and currentIndex < self.length:
            currentIndex += 1
            if currentIndex == self.length:
                return -1
            currentNode = currentNode.next
            currentValue = currentNode.value
        return  currentIndex

    def minValueRecursive(self):
        minValue = float('inf')
        minValue = self.minValue(self.head, minValue)
        print(minValue)
        

    def minValue(self, currentNode, minValue):
        if currentNode == None:
            return minValue
        
        if currentNode.value < minValue:
            minValue = currentNode.value

        return self.minValue(currentNode.next, minValue)



driver = SinglyLinkedlist()
# driver.append('good')
# driver.append('bad')
# driver.append('great')
# driver.append('ugly')
# driver.prepend('starter')
# driver.prepend('another')
# driver.insert('game', 0)
# driver.insert('money', -1)
# driver.insert('last', 8)
# driver.printList()
# driver.removeValue('another')
# driver.deleteAtIndex(-1)
# driver.deleteAtIndex(0)
# driver.deleteAtIndex('')
# driver.deleteAtIndex(0)
# driver.deleteAtIndex(0)
# driver.deleteAtIndex(0)
# driver.deleteAtIndex(0)
# driver.remove('starter')
# driver.remove('starter')
# driver.remove('starter')
# driver.remove('starter')
# driver.remove('')
# driver.remove('')
# driver.printList()
# print(driver.length)
# print(driver.len())
# print(driver.length)
# driver.printListReversedRecursive()
# driver.reverse()

# driver.append(2)
# driver.append(4)
# driver.append(3)
# driver.append(8)
# driver.append(1)
# driver.append(9)
# driver.printList()
# driver.reverseRecursive()
# driver.minValueRecursive()




