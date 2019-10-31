from LinkedLists.singlyLinkedList import SinglyLinkedList, Node


class CircularLinkedList:
    def __init__(self):
        self.linkedList = SinglyLinkedList()

    def append(self, value):
        self.linkedList.append(value)
        self.linkedList.tail.next = self.linkedList.head

    def prepend(self, value):
        self.linkedList.length += 1

        newNode = Node(value)

        self.linkedList.tail.next = newNode
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode

    def insert(self, value, index):
        if index < 0 or index > self.linkedList.length:
            print("Invalid index")
            return
        elif index == 0:
            self.prepend(value)
            return
        elif index == self.linkedList.length:
            self.append(value)
            return

        newNode = Node(value)

        leader = self.__traverseToIndex__(index - 1)
        restOfList = leader.next

        leader.next = newNode
        newNode.next = restOfList
        self.linkedList.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index > self.linkedList.length:
            print("Invalid index")
            return
        elif index == 0:
            temp = self.linkedList.head
            self.linkedList.head = self.linkedList.head.next
            self.linkedList.tail.next = self.linkedList.head
            self.linkedList.length -= 1
            temp.next = None
            return

        leader = self.__traverseToIndex__(index - 1)
        unwantedNode = leader.next

        leader.next = unwantedNode.next

        unwantedNode.next = None

        if index == self.linkedList.length - 1:
            self.linkedList.tail = leader

        self.linkedList.length -= 1

    def __traverseToIndex__(self, index):
        currentNode = self.linkedList.head
        currentIndex = 0
        while currentIndex != index:
            currentNode = currentNode.next
            currentIndex += 1

        return currentNode

    def printList(self):
        circularLinkedList = []
        circularLinkedList.append(self.linkedList.head.value)
        currentNode = self.linkedList.head.next

        while currentNode != self.linkedList.head:
            circularLinkedList.append(currentNode.value)
            currentNode = currentNode.next

        print(circularLinkedList)

    def printListRecursive(self):
        circularLinkedList = []
        self._printListRecursive(self.linkedList.head, circularLinkedList)

        print(circularLinkedList)

    def _printListRecursive(self, currentNode, circularLinkedList):
        circularLinkedList.append(currentNode.value)
        currentNode = currentNode.next

        if currentNode == self.linkedList.head:
            return

        self._printListRecursive(currentNode, circularLinkedList)


ab = CircularLinkedList()

ab.append(12)
ab.append(13)
ab.append(14)
ab.append(15)
ab.append(16)
ab.append(17)
ab.append(18)
ab.prepend(11)
ab.prepend(10)
ab.insert(14.5, 5)
ab.printList()
ab.deleteAtIndex(9)
ab.printList()
ab.printListRecursive()

# print(ab.head)
