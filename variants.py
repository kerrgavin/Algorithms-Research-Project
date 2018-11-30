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

def Yen(G, s):
    initSingleSource(G,s) #number vertices arbitrarily from s
    C = [s]
    D = []
    while C != []:
        for u in G.V:
            edges = G.adj[u]
            if u in C or D != []:
                for uv in edges:
                    D.append(uv)
                    relax(uv.u, uv.v, uv.weight)
        for i in range(len(G.V-1,0,-1)):
            u = G.V[u]
            edges = G.adj[u]
            if u in C or D != []:
                for uv in edges:
                    D.append(uv)
                    relax(uv.u, uv.v, uv.weight)
        C = []
        for k in D:
            C.append(k.u)
            C.append(k.v)
        D = []
