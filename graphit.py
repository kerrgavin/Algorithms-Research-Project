import matplotlib.pyplot as plt
import json

INPUTPATH = "data\\"
OUTPUTPATH = "visualization\\"

def jsonToDict(file):
    data = {}
    with open(INPUTPATH + file, "r") as input:
        data = json.load(input)
    return data


def main():
    data = jsonToDict("test1.json")
    x1 = data["edges"]
    y1 = data["dijkstra"]
    x2 = data["edges"]
    y2 = data["bellmanford"]
    plt.plot(x1, y1)
    plt.plot(x2, y2)

    plt.xlabel("Edges")
    plt.ylabel("Times")
    plt.title("Test")
    plt.savefig(OUTPUTPATH + "test1.png", bbox_inches="tight")


main()
