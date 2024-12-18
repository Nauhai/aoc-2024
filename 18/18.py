import sys
from collections import defaultdict
from heapq import *

input = open(sys.argv[1], 'r').read().strip()
blocks = [b.split(',') for b in input.split('\n')]
blocks = [(int(x), int(y)) for x, y in blocks]

x_max = 70 if len(sys.argv) < 3 else int(sys.argv[2])
y_max = 70 if len(sys.argv) < 4 else int(sys.argv[3])
fallen = 1024 if len(sys.argv) < 5 else int(sys.argv[4])


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def get_graph(x_max, y_max, blocks):
    graph = defaultdict(set) 
    for y in range(y_max+1):
        for x in range(x_max+1):
            for dx, dy in DIRS:
                if 0 <= x+dx <= y_max and 0 <= y+dy <= x_max and (x+dx, y+dy) not in blocks:
                    graph[(x, y)].add((x+dx, y+dy))
    return graph

def shortest(graph, start):
    distances = {p: 0 if p == start else float('inf') for p in graph}
    visited = set()
    pq = [(0, start)]
    heapify(pq)

    while pq:
        dist, pos = heappop(pq)
        if pos in visited:
            continue

        for neighbor in graph[pos]:
            if dist+1 < distances[neighbor]:
                distances[neighbor] = dist+1
                heappush(pq, (dist+1, neighbor))

    return distances


graph = get_graph(x_max, y_max, blocks[:fallen])
start = (0, 0)
end = (x_max, y_max)
distances = shortest(graph, (0, 0))
print(distances[end])


s = 1025
e = len(blocks)
while s < e-1:
    i = (s+e)//2
    graph = get_graph(x_max, y_max, blocks[:i])
    distances = shortest(graph, (0, 0))
    if distances[end] != float('inf'):
        s = i
    else:
        e = i

x, y = blocks[e-1]
print(x, y, sep=',')

