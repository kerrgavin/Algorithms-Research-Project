import math
from graph import *

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
    initSingleSource(G, s)
    S = []
    Q = G.V[:]
    while len(Q) != 0:
        u = extractMin(Q)
        S.append(u)
        for e in G.adj[u]:
            relax(e.u, e.v, e.weight)
    return S
