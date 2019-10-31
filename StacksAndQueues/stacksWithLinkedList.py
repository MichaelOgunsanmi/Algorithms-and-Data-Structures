class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top == None:
            print('Stack Empty')
            return
        print(self.top.value)
        return

    def push(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.top = newNode
            self.bottom = self.top
            self.length += 1
            return

        self.length += 1
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.length == 0:
            self.bottom.value = None
            # self.top.value = None
            return None

        poppedValue = self.top.value

        self.top = self.top.next
        self.length -= 1

        return poppedValue

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def printList(self):
        currentNode = self.top
        stack = []
        while currentNode != None:
            stack.append(currentNode.value)
            currentNode = currentNode.next

        print(stack)


driver = Stack()
driver.push('last element')
driver.push(7)
driver.push(5)
driver.push(34)
driver.push(33)
driver.push(1)
driver.push(77)
driver.push(4321)
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.pop()
driver.peek()
print(driver.bottom.value)
print(driver.top)
driver.printList()
print(driver.length)
