class Graph: 
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node not in self.adjacentList:    
            self.adjacentList[node] = []
            self.numberOfNodes += 1 
    
    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)

        self.adjacentList[node2].append(node1)

    def removeEdge(self, node1, node2):
        self.adjacentList[node1] = list(filter(lambda node: node != node2 ,self.adjacentList[node1]))

        self.adjacentList[node2] = list(filter(lambda node: node != node1 ,self.adjacentList[node2]))
    
    def removeNode(self, node):
        for nodes in self.adjacentList[node]:
            self.removeEdge(node, nodes) 
        del self.adjacentList[node]
        self.numberOfNodes -= 1

    def depthFirstSearchRecursive(self, startNode, result = []):
        result.append(startNode)

        for neighbor in self.adjacentList[startNode]:
            if neighbor not in result:
                result = self.depthFirstSearchRecursive(neighbor, result)

        return result
        
    def depthFirstSearchIterative(self, startNode):
        stack = [startNode]
        result = []

        while len(stack) != 0:
            currentNode = stack.pop()
            if currentNode in result:
                continue
            result.append(currentNode)
            for neighbor in self.adjacentList[currentNode]:
                    stack.append(neighbor)

        return result

    def breadthFirstSearchIterative(self, startNode):
        queue = [startNode]
        result = []

        while len(queue) != 0:
            currentNode = queue.pop(0)
            if currentNode in result:
                continue
            result.append(currentNode)
            for neighbor in self.adjacentList[currentNode]:
                    queue.append(neighbor)

        return result

    def showConnections(self):
        allNodes = self.adjacentList.keys()
        for node in allNodes:
            nodeConnections = self.adjacentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += "{vertex} ".format(vertex=vertex)
            print('{node} --> {connections}'.format(node=node, connections=connections))

driver = Graph()
driver.addVertex('0')
driver.addVertex('1')
driver.addVertex('2')
driver.addVertex('3')
driver.addVertex('4')
driver.addVertex('5')
driver.addVertex('6')
driver.addEdge('3', '1')
driver.addEdge('3', '4')
driver.addEdge('4', '2')
driver.addEdge('4', '5')
driver.addEdge('1', '2')
driver.addEdge('1', '0')
driver.addEdge('0', '2')
driver.addEdge('6', '5')
driver.showConnections()
print(driver.adjacentList)
print(driver.numberOfNodes)
print(driver.depthFirstSearchRecursive('1'))
print(driver.depthFirstSearchIterative('1'))
print(driver.breadthFirstSearchIterative('2'))

