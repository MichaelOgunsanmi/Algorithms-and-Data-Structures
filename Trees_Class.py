# Tree data structure. Binary tree considered

# insert, displaypreorder, displayinorder, displaypostorder
# height, search, findnode, deletedata

class node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None

class Queue:
    def __init__ (self):
        self.items = list()

    def empty(self):
        if self.items == []:
            return False

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        self.items.pop(0)

    def top(self):
        if self.items != []:
            return self.items[-1]

    def size(self):
        return len(self.items)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
         if data < current_node.data:
             if current_node.left_child is None:
                 current_node.left_child = node(data)
                 current_node.left_child.parent = current_node
             else:
                 self._insert(data, current_node.left_child)

         elif data > current_node.data:
            if current_node.right_child is None:
                current_node.right_child = node(data)
                current_node.right_child.parent = current_node
            else:
                self._insert(data, current_node.right_child)

         else:
            print('Value is already present in the tree')

    def displaypreorder(self):
        if self.root is not None:
            self._displaypreorder(self.root)

    def _displaypreorder(self, current_node):
        if current_node != None:
            print(str(current_node.data))
            self._displaypreorder(current_node.left_child)
            self._displaypreorder(current_node.right_child)

    def displayinorder(self):
        if self.root is not None:
            self._displayinorder(self.root)

    def _displayinorder(self, current_node):
        if current_node != None:
            self._displayinorder(current_node.left_child)
            print(str(current_node.data))
            self._displayinorder(current_node.right_child)

    def displaypostorder(self):
        if self.root is not None:
            self._displaypostorder(self.root)

    def _displaypostorder(self, current_node):
        if current_node != None:
            self._displaypostorder(current_node.left_child)
            self._displaypostorder(current_node.right_child)
            print(str(current_node.data))

    def displaylevelorder(self):
        current_node = self.root
        if current_node == None:
            return
        else:
            queue = Queue()
            queue.enqueue(current_node)
            traversal = ""
            while queue.size() > 0:
                traversal += str(queue.top().data) + "-"
                node = queue.dequeue()
                if node.left_child:
                     queue.enqueue(node.left_child)
                if node.right_child:
                    queue.enqueue(node.right_child)
            print(traversal)

    def dislayreverselevelorder(self):


    def getmax(self):
        if self.right_child is None:
            return self.deletedata

    def getmin(self):
        pass

    def size(self):
        pass

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height
        else:
            left_height = self._height(current_node.left_child, current_height + 1)
            right_height = self._height(current_node.right_child, current_height + 1)
            return max(left_height, right_height)

    def search(self, data):                                             #Returns a true or false depending on whether the data is contained in the node
        if self.root is None:
            print('Tree is without any element')
        else:
            return self._search(self.root, data)

    def _search(self, current_node, data):
        if data == current_node.data:
            print(str(data) + ' is present in the tree')
        elif data < current_node.data and current_node.left_child is not None:
            return self._search(current_node.left_child, data)
        elif data > current_node.data and current_node.right_child is not None:
            return self._search(current_node.right_child, data)
        else:
            print(str(data) + ' is not present in the tree')

    def findnode(self, data):
        if self.root is None:
            print('Tree is without any element')
            return None
        else:
            return self._findnode(self.root, data)

    def _findnode(self, current_node, data):
        if current_node.data == data:
            return current_node
        elif data < current_node.data and current_node.left_child != None:
            return self._findnode(current_node.left_child, data)
        elif data > current_node.data and current_node.right_child != None:
            return self._findnode(current_node.right_child, data)
        else:
            print(str(data) + ' is not present in the tree')

    def deletedata(self, data):
        return self.deletenode(self.findnode(data))

    def deletenode(self, node):                         #delete a particular node and do the proper reassignments

        def minvaluenode(n):                            #finds the min node value(farthest left and returns this value)
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        def numberofchildren(n):
            number_of_children = 0
            if n.left_child != None:
                number_of_children += 1
            if n.right_child != None:
                number_of_children += 1
            return number_of_children

        node_parent = node.parent                   #parent of node to be deleted
        node_children = numberofchildren(node)      #gives the number of children available

        if node_children == 0:                      #node has no children
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        elif node_children == 1:
            if node.left_child != None:      # get the single child node
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            elif node_parent.right_child == node:
                node_parent.right_child = child

            child.parent = node_parent      #correct the parent pointer in the node_parent

        if node_children == 2:
            successor = minvaluenode(node.right_child)
            node.data = successor.data
            self.deletenode(successor)




# s = BinarySearchTree()
# s.insert(3)
# s.insert(8)
# s.insert(1)
# s.insert(24)
# s.insert(19)
# s.insert(22)
# s.insert(22)
# print(s.height())
# print('#################')
# s.displaypreorder()
# print('#################')
# s.displayinorder()
# print('#################')
# s.displaypostorder()
# print('#################')
# s.displaylevelorder()
# print('#################')
# s.deletedata(3)
# s.displayinorder()
# print('#################')
# s.deletedata(8)
# s.displayinorder()
# print('#################')
# s.deletedata(1)
# s.displayinorder()
# print('#################')
# s.deletedata(24)
# s.displayinorder()
# print('#################')
# s.deletedata(19)
# s.displayinorder()
# print('#################')
# s.deletedata(22)
# s.height()
