class Element:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.priorityQueue = []

    def enqueue(self, value, priority):
        newElement = Element(value, priority)
        inserted = False 

        index = 0
        while index < len(self.priorityQueue):
            currentItem = self.priorityQueue[index]

            if currentItem[1] > newElement.priority:
                self.priorityQueue.insert(index, [newElement.value, newElement.priority])
                inserted = True 
                break 
            
            index += 1

        if inserted == False: #Here the element has the Lowest priority (priority == 1 == Highest priority while priority > 1 is low priority)
            self.priorityQueue.append([newElement.value, newElement.priority])

    def dequeue(self):
        if self.isEmpty() == True: 
            print('Queue already empty')
            return  
        
        return self.priorityQueue.pop(0)

    def peek(self):
        if self.isEmpty() == True: 
            print('Queue is empty')
            return  
        
        print(self.priorityQueue[0])

    def rear(self):
        if self.isEmpty() == True: 
            print('Queue is empty')
            return  
        
        print(self.priorityQueue[-1])

    def isEmpty(self):
        if len(self.priorityQueue) == 0:
            return True
        return False

    def printQueue(self):
        print(self.priorityQueue)


driver = PriorityQueue()
driver.printQueue()
print(driver.isEmpty())
driver.peek()
driver.enqueue('Second Priority', 2)
driver.enqueue('First Priority', 1)
driver.enqueue('First Priority 2', 1)
driver.enqueue('Second Priority 2', 2)
driver.enqueue('Third Priority', 3)
driver.printQueue()
driver.peek()
driver.rear()
driver.dequeue()
driver.printQueue()
