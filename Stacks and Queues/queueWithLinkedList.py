class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            print('Queue is Empty')
            return 
        print(self.first.value)
    
    def enqueue(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.first = newNode
            self.last = newNode
            self.length += 1
            return
        
        self.length += 1
        self.last.next = newNode
        self.last = newNode
    
    def dequeue(self):
        if self.first == None:
            print('Queue is Empty')
            return 
        
        self.length -= 1
        restOfQueue = self.first.next
        self.first.next = None
        self.first = restOfQueue

    def isEmpty(self):
        if self.length == 0:
            print('True')
            return 
        print('False')
    
    def printQueue(self):
        currentNode = self.first
        queue = []
        while currentNode != None:
            queue.append(currentNode.value)
            currentNode = currentNode.next
        print(queue)

driver = Queue()
driver.isEmpty()
driver.dequeue()
driver.dequeue()
driver.printQueue()
driver.peek()
driver.enqueue('first')
driver.enqueue('second')
driver.enqueue('third')
driver.enqueue('fourth')
driver.enqueue('fifth')
driver.enqueue('sixth')
driver.enqueue('seventh')
driver.peek()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.dequeue()
driver.printQueue()