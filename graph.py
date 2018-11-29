class Graph(object):
    """docstring for Graph."""
    def __init__(self, V = [], E = [], directed = False):
        self.V = V
        self.E = E
        self.directed = directed
        self.adj = {}

    def addVertex(self,value):
        u = Vertex(value=value)
        self.V.append(u)
        self.adj[u] = []

    def addEdge(self,u,v,weight):
        e = Edge(u,v,weight)
        self.adj[u].append(e)
        self.E.append(e)
        if not self.directed:
            f = Edge(v, u, weight)
            if v not in self.adj:
                self.adj[v].append(f)

class Vertex(object):
    """docstring for Vertex."""
    def __init__(self, value = None, d = None, pre = None):
        self.value = value
        self.d = d
        self.pre = pre

class Edge(object):
    """docstring for Edge."""
    def __init__(self, u = None, v = None, weight = None):
        self.u = u
        self.v = v
        self.weight = weight

    def equals(self,other):
        if self.u == other.u and self.v == other.v:
            return True
        return False
