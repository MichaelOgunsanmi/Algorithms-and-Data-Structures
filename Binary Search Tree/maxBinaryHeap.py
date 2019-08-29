class maxBinaryHeap:
    def __init__(self):
        self.values = []
    
    def insert(self, element):
        self.values.append(element)
        self.__bubbleUp__()

    def extractMax(self):
        maxValue = self.values[0]
        lastValue = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = lastValue
            self.__sinkDown__() 
        return maxValue

    def __bubbleUp__(self):
        elementIndex = len(self.values) - 1
        element = self.values[elementIndex]

        while elementIndex > 0:
            parentIndex = (elementIndex - 1) //2
            parent = self.values[parentIndex]
            if element <= parent: break
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
                if leftChild > parent:
                    swap = leftChildIndex

            if rightChildIndex < len(self.values):
                rightChild = self.values[rightChildIndex]
                if (swap == False and rightChild > parent) or (swap != False and rightChild > leftChild):
                    swap = rightChildIndex

            if swap == False: break 

            self.values[parentIndex], self.values[swap] = self.values[swap], self.values[parentIndex]

            parentIndex = swap


driver = maxBinaryHeap()
driver.insert(2)
driver.insert(4)
driver.insert(5)
driver.insert(8)
driver.insert(1)
driver.insert(100)
driver.insert(9)
driver.insert(101)
print(driver.values)
driver.extractMax()
print(driver.values)
