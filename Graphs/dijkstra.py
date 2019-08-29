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

class weightedGraph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    def addEdge(self, node1, node2, weight):
        self.adjacentList[node1].append({ 'node': node2, 'weight': weight})

        self.adjacentList[node2].append({ 'node': node1, 'weight': weight})

    def dijkstra(self, start, end):
        pQueue = priorityQueue()
        distances = {}
        previous = {}
        output = []


        #build up inital state of distances
        for node in self.adjacentList:
            if node == start:
                distances[node] = 0
                pQueue.enqueue(node, 0)
            else:
                distances[node] = float('inf')
                pQueue.enqueue(node, float('inf')) 
            
            previous[node] = None

        #As long as priorityQueue still has values in it
        while len(pQueue.values) != 0:
            smallest = pQueue.dequeue()
            if smallest == end:
                while previous[smallest] != None:
                    output.append(smallest)
                    smallest = previous[smallest]
                break
            if smallest or distances[smallest] != float('inf'):
                for neighbor in self.adjacentList[smallest]:
                    #Calculate new distances to neighbor node
                    candidate = distances[smallest] + neighbor['weight']
                    nextNeighbor = neighbor['node'] 
                    if candidate < distances[nextNeighbor]:
                        #Updating new smallest distance to neighbor
                        distances[nextNeighbor] = candidate
                        #Updating previous - How we got to neighbor
                        previous[nextNeighbor] = smallest
                        #enqueue in priorityQueue with new priority (new sum)
                        pQueue.enqueue(nextNeighbor, candidate)
        output.append(smallest)
        return output[::-1], 'Shortest distance = {distance}'.format(distance = distances[end])
            

        
        







driver = weightedGraph()
driver.addVertex('A')
driver.addVertex('B')
driver.addVertex('C')
driver.addVertex('D')
driver.addVertex('E')
driver.addVertex('F')
driver.addEdge('A', 'B', 4)
driver.addEdge('A', 'C', 2)
driver.addEdge('B', 'E', 3)
driver.addEdge('C', 'D', 2)
driver.addEdge('C', 'F', 4)
driver.addEdge('D', 'E', 3)
driver.addEdge('D', 'F', 1)
driver.addEdge('E', 'F', 1)
# print(driver.adjacentList)
print(driver.dijkstra('A', 'E'))
