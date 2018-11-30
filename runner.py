from graph import *
import pickle
import variants
import argparse
import time
import json

INPUTPATH = "graphs\\"
OUTPUTPATH = "data\\"

def readGraphList(f):
    file = open(INPUTPATH + f, 'rb')
    G = pickle.load(file)
    file.close()
    return G

def writeData(data, file):
    with open(OUTPUTPATH+file, "w") as output:
        json.dump(data, output, indent = 4)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('f', action='store', type = str, help='Input file name')
    parser.add_argument('o', action='store', type = str, help='Output file name')
    return parser.parse_args()

def getTimeDijkstra(G):
    times = []
    for i in range(0,3):
        start = round(time.clock() * 10000)
        variants.dijkstra(G, G.V[0])
        end = round(time.clock() * 10000)
        times.append(end-start)
    avg = (times[0] + times[0] + times[0])/3
    return avg

def getTimeBellmanFord(G):
    times = []
    for i in range(0,3):
        start = round(time.clock() * 10000)
        variants.bellmanFord(G, G.V[0])
        end = round(time.clock() * 10000)
        times.append(end-start)
    avg = (times[0] + times[0] + times[0])/3
    return avg

def main():
    data = {"vertices":0, "dijkstra": [], "bellmanford": [], "edges": []}
    args = parse()
    print("Loading graph list " + args.f + "...")
    graphList = readGraphList(args.f)
    print("Loading Complete.")
    print("Beginning to calculate run time.")
    for G in graphList:
        data["vertices"] = len(G.V)
        data["edges"].append(len(G.E))

        print("Graph info: \n\tDirected: " + str(G.directed) + "\n\tVertex Count: " + str(len(G.V)) + "\n\tEdge Count: " + str(len(G.E)))
        print("Calculating average time for shortest path...")

        avg = getTimeDijkstra(G)
        data["dijkstra"].append(avg)

        print("Dijkstra Run Time: ", data["dijkstra"][-1])

        avg = getTimeBellmanFord(G)
        data["bellmanford"].append(avg)
        print("Bellman-Ford Run Time: ", data["bellmanford"][-1])
        print("Solution complete.")

        print("Writing data to " + args.o + "...")
        writeData(data, args.o)
        print("Data written")

main()
