class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def peek(self):
        if self.length == 0:
            print('Stack is Empty')
            return
        print(self.stack[-1])
        return 
    
    def push(self, value):
        self.length += 1
        self.stack.append(value)
    
    def pop(self):
        if self.length == 0:
            print('Stack is Empty')
            return
        self.length -= 1
        return self.stack.pop()
    
    def isEmpty(self):
        if self.length == 0:
            return True
        return False
    
    def printList(self):
        print(self.stack[::-1])


# driver = Stack()
# print(driver.isEmpty())
# # driver.pop()
# # driver.peek()
# driver.push('bottom')
# # driver.peek()
# driver.push('4')
# driver.peek()
# driver.push('8')
# driver.push('12')
# driver.push('top')
# driver.push('top2to be popped')
# driver.push('top2to be removed')
# driver.pop()
# driver.pop()
# driver.peek()
# driver.printList()

