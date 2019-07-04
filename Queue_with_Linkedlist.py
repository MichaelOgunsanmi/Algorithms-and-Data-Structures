# Queue with Linkedlist

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedlistQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def display(self):
        if self.head is None:
            print('Queue is empty')
            return
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next

    def empty(self):
        if self.head is None:
            print('Queue is empty')
        else:
            print('Queue is not empty')

    def enqueue(self, newnode):
        self.size += 1
        if self.head is None:
            self.head = newnode
        else:
            current_node = self.head     #ben ali michael dami
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = newnode

    def dequeue(self):
        if self.head is None:
            print('Queue is empty')
            return
        else:
            current_node = self.head
            self.head = current_node.next
            self.size -= 1
            return current_node.data

    def top(self):
        if self.head is None:
            print('Queue is empty')
        else:
            print(self.head.data)


# firstnode = node(56)
# secondnode = node('Michael')
# thirdnode = node('Titilayo')
# s = LinkedlistQueue()
# s.empty()
# s.enqueue(firstnode)
# j = s.size
# print(j)
# s.enqueue(secondnode)
# j = s.size
# print(j)
# s.enqueue(thirdnode)
# j = s.size
# print(j)
# s.display()
# s.empty()
# s.dequeue()
# j = s.size
# print(j)
# s.display()
# s.dequeue()
# j = s.size
# print(j)
# s.display()
# s.dequeue()
# j = s.size
# print(j)
# s.display()
# s.dequeue()
# j = s.size
# print(j)
# s.display()
