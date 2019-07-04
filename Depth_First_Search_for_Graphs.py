#DFS for Graphs

class node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencieslist = []
        self.visited = False

def DepthFirstSearch(node):
    node.visited = True
    print(node.name)
    for adjacencies in node.adjacencieslist:
        if not adjacencies.visited:
            DepthFirstSearch(adjacencies)

node1 = node('A')
node2 = node('B')
node3 = node('C')
node4 = node('D')
node5 = node('E')

node1.adjacencieslist.append(node2)
node1.adjacencieslist.append(node3)
node2.adjacencieslist.append(node4)
node4.adjacencieslist.append(node5)

s = DepthFirstSearch(node1)
