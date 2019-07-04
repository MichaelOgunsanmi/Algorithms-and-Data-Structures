# Stacks with Linkedlist

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedlistStacks:
    def __init__(self):
        self.head = None
        self.size = 0

    def display(self):
        if self.head is None:
            print('Stack is empty')
            return
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next

    def push(self, new_node):
        self.size += 1
        if self.head == None:
            self.head = new_node
            return
        else:
            current_node = self.head      #Similar to Binsert
            self.head = new_node
            self.head.next = current_node
            del current_node

    def pop(self):
        if self.head is None:
            print('Stack is empty')
            return
        else:
            popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped

    def empty(self):
        if self.head is None:
            print('Stack is empty')
        else:
            print('Stack is not empty')

    def top(self):
        if self.head is None:
            print('Stack is empty')
        else:
            print(self.head.data)

# firstnode = node(23)
# secondnode = node(12)
# thirdnode = node('Michael')
#
# s = LinkedlistStacks()
# s.top()
# s.push(firstnode)
# print('###################')
# print(s.size)
# s.top()
# s.push(secondnode)
# print('###################')
# print(s.size)
# s.top()
# s.push(thirdnode)
# print('###################')
# print(s.size)
# s.top()
# s.pop()
# print('###################')
# print(s.size)
# s.top()
# s.pop()
# print('###################')
# print(s.size)
# s.top()
# s.pop()
# print('###################')
# print(s.size)
# s.top()
# s.pop()
# print('###################')
# print(s.size)
# s.empty()
# s.display()
