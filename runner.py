from graph import *
import pickle
import variants
import argparse
import time

PATH = "graphs\\"

def readGraphList(f):
    file = open(f, 'rb')
    G = pickle.load(file)
    file.close()
    return G


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('f', action='store', type = str, help='File name')
    return parser.parse_args()


def main():
    args = parse()
    print("Loading graph list" + args.f + "...")
    graphList = readGraphList(PATH + args.f)
    print("Loading Complete.")
    print("Beginning to calculate run time.")
    for G in graphList:
        print("Graph info: \n\tDirected: " + str(G.directed) + "\n\tVertex Count: " + str(len(G.V)) + "\n\tEdge Count: " + str(len(G.E)))
        print("Solving for shortest path...")
        start = round(time.clock() * 10000)
        print(start)
        variants.dijkstra(G, G.V[0])
        end = round(time.clock() * 10000)
        print()
        print(end)
        print("Run Time: ", str(end-start))
        print(variants.bellmanFord(G, G.V[0]))
        print("Solution complete.")

main()
