# def minDepth(self, root) -> int:
#     return self.minDepthRec(root, 1)
#
#
# def minDepthRec(self, currentNode, count):
#     if currentNode is None:
#         return count - 1
#
#     if self.isLeaf(currentNode):
#         return count
#
#     return min(self.minDepthRec(currentNode.left, count + 1),
#                self.minDepthRec(currentNode.right, count + 1))
#
#
# def isLeaf(self, currentNode):
#     return currentNode.left is None and currentNode.right is None


# def mergeTrees(firstTree, secondTree):
#     if firstTree is None:
#         return secondTree
#
#     if secondTree is None:
#         return firstTree
#
#     mergeTreesRec(firstTree, secondTree)
#
#     return firstTree
#
#
# def mergeTreesRec(firstTree, secondTree):
#     if firstTree.left is None and secondTree.left is not None:
#         firstTree.left = secondTree.left
#         return
#
#     if firstTree.left is not None and secondTree.left is None:
#         return
#
#     if firstTree.right is None and secondTree.right is not None:
#         firstTree.right = secondTree.right
#         return
#
#     if firstTree.right is not None and secondTree.right is None:
#         return
#
#     firstTree.val = firstTree.val + secondTree.val
#
#     if firstTree.left is not None and secondTree.left is not None:
#         mergeTreesRec(firstTree.left, secondTree.left)
#
#     if firstTree.right is not None and secondTree.right is not None:
#         mergeTreesRec(firstTree.right, secondTree.right)
#
#
# def isLeaf(currentNode):
#     return currentNode.left is None and currentNode.right is None
#
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# # a = TreeNode(5)
# # a.left = TreeNode(6)
# # a.left.left = TreeNode(6)
# # a.left.left.left = TreeNode(6)
# # a.right = TreeNode(7)
# # a.right.left = TreeNode(8)
# # a.right.right = TreeNode(9)
# #
# # b = TreeNode(7)
# # b.left = TreeNode(3)
# # b.left.left = TreeNode(4)
# # b.left.left.left = TreeNode(2)
# # b.right = TreeNode(4)
# # b.right.left = TreeNode(1)
# # b.right.right = TreeNode(3)
# #
# #
# # c = mergeTrees(a, b)
# #
# # print(c.val)
# # print(c.left.val)
# # print(c.left.left.val)
# # print(c.left.left.left.val)
# # print(c.right.val)
# # print(c.right.left.val)
# # print(c.right.right.val)
#
# a = TreeNode(5)
# a.left = TreeNode(6)
# a.left.left = TreeNode(6)
# a.right = TreeNode(7)
# a.right.left = TreeNode(8)
# a.right.right = TreeNode(9)
#
# b = TreeNode(7)
# b.left = TreeNode(3)
# b.left.left = TreeNode(4)
# b.left.left.left = TreeNode(2)
# b.right = TreeNode(4)
#
# c = mergeTrees(a, b)


def a (b , c):
    k = b*2
    y = c / 2
    r = k * y
    return r

a (1, 4)

# print(c.right.val)