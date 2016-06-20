#Uses python3

import sys


def acyclic(adj):
    while sink_exists(adj):
        remove(sink_exists(adj))
    return 0 if len(adj) == 0 else 1

def sink_exists(adj):
    for node in adj:
        if not node:
            return node
    return false

def remove(node):
    for vertex in adj:
        if node in vertex:
             vertex.remove(node)
    adj.remove(node)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
