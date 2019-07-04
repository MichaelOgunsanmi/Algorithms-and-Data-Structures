# Doubly Linked List

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('List is Empty')
            return
        current_node = self.head
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def length(self):
        current_node = self.head
        total = 0
        while current_node != None:
            total += 1
            current_node = current_node.next
        return total

    def Einsert(self, new_node):
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            current_node = self.head #56 7 3333333333
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None

    def Binsert(self, new_node):
            current_node = self.head
            self.head = new_node
            new_node.prev = None
            new_node.next = current_node
            del current_node

    def Iinsert(self, new_node, index):
        if index is 0:
            print('Can only insert in between nodes. Use the Binsert or Einsert functions')
            return
        elif index < 0 or index >= self.length():
            print('Invalid Position')
            return
        elif index == (self.length() - 1):
            print('Can only insert in between nodes. Use the Binsert or Einsert functions')
            return
        else:
            current_node = self.head      #ben sally cr7 nau may
            current_index = 0
            while current_index != index:
                current_index += 1
                current_node = current_node.next
            previous_node = current_node.data
            print(previous_node.data)
            print(current_node.data)
            # temp = current_node
            # current_node = new_node
            # previous_node = current_node.prev
            # current_node = previous_node.next
            # temp = current_node.next
            # del temp




firstnode = node(56)
secondnode = node(7)
thirdnode = node(3333333333333333)
doublylinkedlist = DoublyLinkedList()
doublylinkedlist.Einsert(firstnode)
doublylinkedlist.Einsert(secondnode)
doublylinkedlist.Einsert(thirdnode)
doublylinkedlist.display()
print('#########################')
thirdnode = node('Rose')
fourthnode = node('Riverrun')
doublylinkedlist.Binsert(thirdnode)
doublylinkedlist.Binsert(fourthnode)
doublylinkedlist.display()
print('#########################')
print(doublylinkedlist.length())
print('#########################')
fifthnode = node(8)
doublylinkedlist.Iinsert(fifthnode, 1)
doublylinkedlist.display()
