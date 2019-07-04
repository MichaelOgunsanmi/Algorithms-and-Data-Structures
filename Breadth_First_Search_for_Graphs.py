# BFS for Graphs

# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = list()        #a list of each vertex's neighbour
        self.distance = 100000000000000 #a large value
        self.color = 'black' #to indicate that the node is unvisited

    def addneighbour(self, vertex):
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)
            self.neighbours.sort()

class Graph:
    vertices = {}

    def addvertex(self, vertex):
        if isinstance(vertex, vertex) and vertex.name not in self.vertices:
            delf.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def addedge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            for key, value in self.vertices.items():
                if key == vertex1:
                    value.addneighbour(vertex2)
                if key == vertex2:
                    value.addneighbour(vertex1)
            return True
        else:
            return False

    def display(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + " " + str(self.vertices).)

    def
