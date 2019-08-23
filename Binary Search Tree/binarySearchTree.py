class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        
        if self.root == None:
            self.root = newNode
            return

        currentNode = self.root
        while currentNode != None:
            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode.left = newNode
                    return
                currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    currentNode.right = newNode
                    return
                currentNode = currentNode.right 

    def lookup(self, value):
        if self.root == None:
            print('Tree contains no element so "{value}" not in tree'.format(value=value))
            return

        currentNode = self.root
        while currentNode != None:
            if currentNode.value == value:
                print('Found {value}'.format(value = value))
                return
            elif value < currentNode.value:
                    currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        print('{value} not in the Tree'.format(value = value))

    def remove(self, value):
        if self.root == None:
            print('Tree contains no element do "{value}" cannot be removed from the tree'.format(value=value))
            return 
        
        #if value is in root node
        if self.root.value == value:
            if self.root.left == None and self.root.right == None:
                self.root = None
            elif self.root.left != None and self.root.right == None:
                self.root = self.root.left
            elif self.root.left == None and self.root.right != None:
                self.root = self.root.right
            elif self.root.left != None and self.root.right != None:
                successorParent = self.root
                successor = successorParent.right

                while successor.left != None:
                    successorParent = successor
                    successor = successor.left

                self.root.value = successor.value

                if successor.right != None:
                    if successorParent.value > successor.value:
                        successorParent.left = successor.right
                    elif successorParent.value < successor.value:
                        successorParent.right = successor.right
                else:
                    if successorParent.value > successor.value:
                        successorParent.left = None
                    else:
                        successorParent.right = None
            
            return 

        
        # Lookup for node to be removed if node is part o f rest of Tree
        currentNode = self.root
        parentNode = None

        while currentNode != None:
            if currentNode.value == value:
                break 
            elif value < currentNode.value :
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        
        if currentNode == None:
            print('Node not in the tree')
            return
        
        #Case 1: removeNode is a Leaf node
        if currentNode.left == None and currentNode.right == None:
            if value == parentNode.left.value:
                parentNode.left = None
            else:
                parentNode.right = None
            return

        #Case 2: removeNode has only one child

        #Case 2a: removeNode has only a left Child:
        if currentNode.left != None and currentNode.right == None:
            if value == parentNode.left.value:
                parentNode.left = currentNode.left
            else:
                parentNode.right = currentNode.left
            return

        #Case 2b: removeNode has only a right Child:
        if currentNode.left == None and currentNode.right != None:
            if value == parentNode.left.value:
                parentNode.left = currentNode.right
            else:
                parentNode.right = currentNode.right
            return 

        #Case 3: removeNode has left and right children:
        #We could solve by replacing removeNode with largest in left sub-tree or smallest in right sub-tree. 

        #To replace with smallest in right sub tree, get next node. Check if nextNode.left == None. if not traverse through left node until None and then replace.
        successorParent = currentNode
        successor = successorParent.right

        while successor.left != None:
            successorParent = successor
            successor = successor.left

        currentNode.value = successor.value

        if successor.right != None:
            if successorParent.value > successor.value:
                successorParent.left = successor.right
            elif successorParent.value < successor.value:
                successorParent.right = successor.right
        else:
            if successorParent.value > successor.value:
                successorParent.left = None
            else:
                successorParent.right = None

        
    def breadthFirstSearch(self):
        currentNode = self.root
        treeElements = []
        queue = [currentNode]

        while len(queue) > 0:
            currentNode = queue.pop(0)
            treeElements.append(currentNode.value)
            
            if currentNode.left != None:
                queue.append(currentNode.left)
            
            if currentNode.right!= None:
                queue.append(currentNode.right)
        
        print(treeElements)

    def depthFirstSearchPreOrder(self):
        currentNode = self.root
        treeElements = []
        stack = []

        if currentNode == None:
            print(stack)
            return  

        stack.append(currentNode)

        while len(stack) > 0:
            currentNode = stack.pop()
            treeElements.append(currentNode.value)

            if currentNode.right != None:
                stack.append(currentNode.right)
            
            if currentNode.left != None:
                stack.append(currentNode.left)

        print(treeElements)

    def depthFirstSearchPostOrder(self):
        currentNode = self.root
        treeElements = []
        stack = []

        if currentNode == None:
            print(stack)
            return  
        
        stack.append(currentNode)

        while len(stack) > 0:
            currentNode = stack.pop()
            treeElements.insert(0,currentNode.value)

            if currentNode.left != None:
                stack.append(currentNode.left) 

            if currentNode.right != None:
                stack.append(currentNode.right)

        print(treeElements)

    def depthFirstSearchInOrder(self):
        currentNode = self.root
        treeElements = []
        stack = []

        if currentNode == None:
            print(stack)
            return 
        
        while True:
            if currentNode != None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                if len(stack) == 0:
                    break
                currentNode = stack.pop()
                treeElements.append(currentNode.value)
                currentNode = currentNode.right 
        
        print(treeElements)

    def recursiveBreadthFirstSearch(self, queue, treeElements):
        if len(queue) == 0:
            return treeElements

        currentNode = queue.pop(0)
        treeElements.append(currentNode.value)

        if currentNode.left != None:
            queue.append(currentNode.left)

        if currentNode.right != None:
            queue.append(currentNode.right)

        return self.recursiveBreadthFirstSearch(queue, treeElements)

    def recursiveDepthFirstSearchPreOrder(self):
        return self.traversePreOrder(self.root, [])

    def traversePreOrder(self, currentNode, treeElements):
        treeElements.append(currentNode.value)

        if currentNode.left != None:
            self.traversePreOrder(currentNode.left, treeElements)

        if currentNode.right != None:
            self.traversePreOrder(currentNode.right, treeElements)

        return treeElements

    def recursiveDepthFirstSearchPostOrder(self):
        return self.traversePostOrder(self.root, [])

    def traversePostOrder(self, currentNode, treeElements):
        if currentNode.left != None:
            self.traversePostOrder(currentNode.left, treeElements)

        if currentNode.right != None:
            self.traversePostOrder(currentNode.right, treeElements)

        treeElements.append(currentNode.value)
        return treeElements

    def recursiveDepthFirstSearchInOrder(self):
        return self.traverseInOrder(self.root, [])

    def traverseInOrder(self, currentNode, treeElements):
        if currentNode.left != None:
            self.traverseInOrder(currentNode.left, treeElements)

        treeElements.append(currentNode.value)

        if currentNode.right != None:
            self.traverseInOrder(currentNode.right, treeElements)

        
        return treeElements
        
        




driver = BinarySearchTree()
driver.lookup(100) 
driver.insert(9)
driver.insert(4)
driver.insert(1)
driver.insert(6)
driver.insert(5)
driver.insert(8)
driver.insert(20)
driver.insert(15)
driver.lookup(100)
driver.insert(170)
driver.breadthFirstSearch()
print('Breadth First Search Recursive', driver.recursiveBreadthFirstSearch([driver.root], []))
driver.depthFirstSearchPreOrder()
print('Depth First Search Recursive PreOrder', driver.recursiveDepthFirstSearchPreOrder())
driver.depthFirstSearchInOrder()
print('Depth First Search Recursive InOrder', driver.recursiveDepthFirstSearchInOrder())
driver.depthFirstSearchPostOrder()
print('Depth First Search Recursive PostOrder', driver.recursiveDepthFirstSearchPostOrder())
