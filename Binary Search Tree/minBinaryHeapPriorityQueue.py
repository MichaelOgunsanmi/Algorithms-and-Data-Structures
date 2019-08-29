class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class priorityQueue:
    def __init__(self):
        self.values = []
    
    def enqueue(self, value, priority):
        newNode = Node(value, priority)
        self.values.append(newNode)
        self.__bubbleUp__()

    def dequeue(self):
        minValue = self.values[0]
        lastValue = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = lastValue
            self.__sinkDown__() 
        return minValue.value

    def __bubbleUp__(self):
        elementIndex = len(self.values) - 1
        element = self.values[elementIndex]

        while elementIndex > 0:
            parentIndex = (elementIndex - 1) //2
            parent = self.values[parentIndex]
            if element.priority >= parent.priority: break
            self.values[parentIndex], self.values[elementIndex] = element, parent
            elementIndex = parentIndex

    def __sinkDown__(self):
        parentIndex = 0
        parent = self.values[parentIndex]

        while True:
            leftChildIndex = (2 * parentIndex) + 1
            rightChildIndex = (2 * parentIndex) + 2

            swap = False

            if leftChildIndex < len(self.values):
                leftChild = self.values[leftChildIndex]
                if leftChild.priority < parent.priority:
                    swap = leftChildIndex

            if rightChildIndex < len(self.values):
                rightChild = self.values[rightChildIndex]
                if (swap == False and rightChild.priority < parent.priority) or (swap != False and rightChild.priority < leftChild.priority):
                    swap = rightChildIndex

            if swap == False: break 

            self.values[parentIndex], self.values[swap] = self.values[swap], self.values[parentIndex]

            parentIndex = swap


ER = priorityQueue()
ER.enqueue('common cold', 5)
ER.enqueue('gunshot wound', 1)
ER.enqueue('high fever', 4)
ER.enqueue('broken arm', 2)
ER.enqueue('glass in foot', 3)
for elem in ER.values:
    print(elem.value, elem.priority)
print('xxxxxxxx')
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())