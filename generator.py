from graph import *
import pickle
import random
import argparse

PATH = "graphs\\"

def pickleGraphList(G, f):
    file = open(f, 'wb')
    pickle.dump(G, file)
    file.close()

def genGraph(num, edgeCap, weightMax, weightMin = 0):
    G = Graph(V=[],E=[],directed = True)
    for i in range(0, num):
        G.addVertex(i)
    for u in G.V:
        for i in range(edgeCap):
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


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('v', action='store', type = int, help='Number of vertices in the generated graph')
    parser.add_argument('max', action='store', type = int, help='Maximum weight for a given edge')
    parser.add_argument('--min', dest='min', type = int, action='store', default=0, help='Minimum value for a given edge (default = 0)')
    parser.add_argument('f', action='store', type = str, help='File name')
    return parser.parse_args()

def main():
    args = parse()
    print("Generating graph list " +  args.f + "...")
    graphList = []
    for i in range(1, args.v):
        G = genGraph(args.v, i, args.max, args.min)
        graphList.append(G)
    print("Generation complete.")
    pickleGraphList(graphList, PATH + str(args.f))
    print("File save")


main()
