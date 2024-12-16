import sys
from collections import defaultdict
from heapq import *

input = open(sys.argv[1], 'r').read().strip()
grid = input.split('\n')
width = len(grid)
height = len(grid[0])

tiles = set()
for i in range(width):
    for j in range(height):
        if grid[i][j] != '#':
            tiles.add((i, j))

            match grid[i][j]:
                case 'S':
                    starting_pos = (i, j)
                case 'E':
                    ending_pos = (i, j)

starting_dir = (0, 1)

graph = defaultdict(set)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for tile in tiles:
    i, j = tile
    for di, dj in DIRS:
        if (i+di, j+dj) in tiles:
            graph[tile].add((i+di, j+dj))

def shortest(graph, starting, dir, ending):
    distances = {tile: 0 if tile == starting else float('inf') for tile in graph}
    predecessors = {tile: set() for tile in graph}
    visited = set()

    pq = [(0, starting, dir)]
    heapify(pq)
    
    while pq:
        dist, pos, dir = heappop(pq)
        if pos in visited:
            continue
        
        i, j = pos
        for neighbor in graph[pos]:
            ni, nj = neighbor
            new_dir = (ni-i, nj-j)

            new_dist = dist+1
            if new_dir != dir:
                new_dist += 1000
            
            if new_dist < distances[neighbor]:
                predecessors[neighbor] = {pos}
                distances[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor, new_dir))
            if new_dist == distances[neighbor]:
                predecessors[neighbor].add(pos)

    return distances, predecessors

d, p = shortest(graph, starting_pos, starting_dir, ending_pos)
print(d[ending_pos])

