from graph import *
try:
    import cPickle as pickle
except:
    import pickle
import random
import argparse

PATH = "graphs\\"

def pickleGraphList(G, f):
    file = open(f, 'ab')
    pickle.dump(G, file)
    file.close()

def genGraph(num, edgeCap, weightMax, weightMin = 0):
    G = Graph(V=[],E=[],directed = True)
    for i in range(0, num):
        G.addVertex(i)
    Q = G.V[:]
    while len(Q) > 0:
        v = Q[0]
        while not v == Q[0]:
            v = Q[random.randint(0,len()-1)]
        G.addEdge(Q[0], v, random.randint(weightMin, weightMax))
        Q.pop(0)
    for u in G.V:
        for i in range(edgeCap - 1):
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
    # parser.add_argument('e', action='store', type = int, help='Number of edges in the graph')
    parser.add_argument('max', action='store', type = int, help='Maximum weight for a given edge')
    parser.add_argument('--min', dest='min', type = int, action='store', default=0, help='Minimum value for a given edge (default = 0)')
    parser.add_argument('f', action='store', type = str, help='File name')
    return parser.parse_args()

def main():
    args = parse()
    print("Generating data set " +  args.f + "...")
    for i in range(1, 13):
        print(i)
        if 300%(25*i) == 0:
            print("Generating graph with vertex count " + str(i * 25) + "...")
            G = genGraph(25 * i, 300//(25*1), args.max, args.min)
            print("Generation complete.")
            print("Saving to file...")
            pickleGraphList(G, PATH + str(args.f))
            print("File saved.")
            G = None
    print("Data set generated and saved.")


main()
