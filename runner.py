from graph import *
import random
import variants


def genGraph(num, edgeCap, weightMax, weightMin = 0):
    G = Graph(directed = True)
    for i in range(0, num):
        G.addVertex(i)
    for u in G.V:
        edgeNum = random.randint(1, edgeCap)
        for i in range(edgeNum):
            success = False
            while not success:
                v = G.V[random.randint(0,len(G.V)-1)]

                if u == v:
                    continue

                edge = Edge(u,v,random.randint(weightMin, weightMax))
                same = False

                for e in G.adj[u]:
                    if edge.equals(e):
                        same = True
                        break

                if not same:
                    G.addEdge(edge.u, edge.v, weight = edge.weight)
                    success = True
    return G

def main():
    G = genGraph(100, 10, 5)

    for v in variants.dijkstra(G, G.V[0]):
        print(v.value, end = ", ")
    print()
    print(variants.bellmanFord(G, G.V[0]))

main()
