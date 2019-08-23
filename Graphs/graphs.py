class Graph: 
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):    
        self.adjacentList[node] = []
        self.numberOfNodes += 1 
    
    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(int(node2))

        self.adjacentList[node2].append(int(node1))

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

