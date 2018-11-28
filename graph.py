class Graph(object):
    """docstring for Graph."""
    def __init__(self, V = [], E = [], directed = False):
        self.V = V
        self.E = E
        self.directed = directed
        self.adj = {}

    def addEdge(u,v,weight):
        e = Edge(u,v,weight)
        if u not in self.adj:
            self.adj[u] = [e]
        else:
            self.adj[u].append(e)
        if not directed:
            f = Edge(v, u, weight)
            if v not in self.adj:
                self.adj[v] = [f]
            else:
                self.adj[u].append(f)

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
