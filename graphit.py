import matplotlib.pyplot as plt
import json
import argparse

INPUTPATH = "data\\"
OUTPUTPATH = "visualization\\"

def jsonToDict(file):
    data = {}
    with open(INPUTPATH + file, "r") as input:
        data = json.load(input)
    return data

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('f', action='store', type = str, help='Input file name')
    parser.add_argument('o', action='store', type = str, help='Output file name')
    return parser.parse_args()

def main():
    args = parse()
    print("Reading in data from" + args.f + "...")
    data = jsonToDict(args.f)
    print("Data read.")

    print("Parsing X axis...")
    x1 = data["edges"]
    x2 = data["edges"]
    print("Parsing Y axis...")
    y1 = data["dijkstra"]
    y2 = data["bellmanford"]
    print("Axes plotted.")

    print("Plotting graph...")
    plt.plot(x1, y1, label="Dijkstra")
    plt.plot(x2, y2, label="Bellman-Ford")
    print("Graph plotted.")
    plt.legend(loc='best')
    print("Generating graph labels...")
    plt.xlabel("Edges")
    plt.ylabel("Times")
    plt.title("Test")
    print("Labels generated.")

    print("Saving to " + args.o + "...")
    plt.savefig(OUTPUTPATH + args.o, bbox_inches="tight")
    print("File saved.")


main()
