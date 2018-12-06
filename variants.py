import math
from graph import *
from fibheap import *

def initSingleSource(G, s):
    for v in G.V:
        v.d = math.inf
        v.pre = None
    s.d = 0

def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pre = u

def extractMin(Q):
    min = 0
    for index in range(0,len(Q)):
        if Q[min].d > Q[index].d:
            min = index
    return Q.pop(min)


def bellmanFord(G, s):
    initSingleSource(G, s)
    for i in range(0, len(G.V)):
        for e in G.E:
            relax(e.u, e.v, e.weight)
    for e in G.E:
        if e.v.d > e.u.d + e.weight:
            return False
    return True

def dijkstra(G, s):
    # print(G.adj)
    initSingleSource(G, s)
    S = []
    Q = G.V[:]
    while len(Q) != 0:
        u = extractMin(Q)
        S.append(u)
        for e in G.getAdj(u):
            relax(e.u, e.v, e.weight)
    return S

def Yen(G, s):
    initSingleSource(G,s) #number vertices arbitrarily from s
    C = [s]
    D = []
    while C != []:
        for u in G.V:
            edges = G.getAdj(u)
            if u in C or D != []:
                for uv in edges:
                    D.append(uv)
                    relax(uv.u, uv.v, uv.weight)
        for i in range(len(G.V)-1,0,-1):
            u = G.V[i]
            edges = G.getAdj(u)
            if u in C or D != []:
                for uv in edges:
                    D.append(uv)
                    relax(uv.u, uv.v, uv.weight)
        C = []
        for k in D:
            C.append(k.u)
            C.append(k.v)
        D = []

# def fibDijkstra(G, s):
#     initSingleSource(G, s)
#     S = []
#     Q = FibonacciHeap()
#     for v in G.V:
#         Q.insert(v)
#         print(Q.find_min().key.d)
#     print([x.key.value for x in Q.iterate(Q.root_list)])
#
#     while Q.total_nodes != 0:
#
#         u = Q.extract_min()
#
#         if u is not None:
#             for e in G.adj[u.key]:
#                 print("Connections: ", str(e.v.value))
#             S.append(u.key)
#             for e in G.adj[u.key]:
#                 relax(e.u, e.v, e.weight)
#     return S

def fibRelax(u, v, w, heap, h):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pre = u
        heap.decrease_key(h,w)

def fibDijkstra(G, s):
    n = len(G.V)    #intentionally 1 more than the number of vertices, keep the 0th entry free for convenience
    visited = [False]*(n)
    distance = [math.inf]*n

    heapNodes = [None]*(n+1)
    heap = FibonacciHeap()
    for i in range(1, n+1):
        heapNodes[i] = heap.insert(math.inf, i)     # distance, label

    distance[s.value] = 0
    heap.decrease_key(heapNodes[s.value + 1], 0)
    print([x.key for x in heap.iterate(heap.root_list)])
    S = []
    while heap.total_nodes:
        current = heap.extract_min().value - 1

        visited[current] = True
        S.append(current)
        for e in G.adj[current]:
            neighbor = e.v.value
            cost = e.weight
            if not visited[neighbor]:
                if distance[current] + cost < distance[neighbor]:
                    distance[neighbor] = distance[current] + cost
                    heap.decrease_key(heapNodes[neighbor + 1], distance[neighbor])
        # print([x.value for x in heap.iterate(heap.root_list)])


    return S

# def fibDijkstra(G, s):
#     n = len(G.V)    #intentionally 1 more than the number of vertices, keep the 0th entry free for convenience
#     visited = [False]*n
#     initSingleSource(G, s)
#     S = []
#     heapNodes = []
#     heap = FibonacciHeap()
#     heapNodes.append(None)
#     for i in G.V:
#         print(i.value)
#         heapNodes.append(heap.insert(i))
#         print([x.key.value for x in heap.iterate(heap.root_list)])     # distance, label
#         print("heap: ", heapNodes)
#     heap.decrease_key(heapNodes[1], 0)
#
#     while heap.total_nodes:
#         current = heap.extract_min().key
#         if current is not None:
#             print([x.key.value for x in heap.iterate(heap.root_list)])
#             visited[current.value] = True
#             S.append(current)
#             for e in G.adj[current]:
#                 if not visited[e.v.value]:
#                     fibRelax(e.u, e.v, e.weight, heap, heapNodes[e.v.value+1])
#     return S
