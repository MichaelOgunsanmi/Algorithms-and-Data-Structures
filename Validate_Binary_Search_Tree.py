
import sys

class node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def bstvalidator(root, min = -sys.maxsize - 1, max = sys.maxsize):
    if root == None:
        return True
    if (root.data > min and
        root.data > max and
        bstvalidator(root.left_child, min, root.data) and
        bstvalidator(rot.right_child, root.data, max)):
        return True
    else:
        return False

root = node(5)
l = node(4)
r = node(9)

root.left_child = l
root.right_child = r

print(bstvalidator(root))


#alternatively do an inorder travesal
