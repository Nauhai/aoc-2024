import sys
from collections import defaultdict

input = open(sys.argv[1], 'r').read().strip()
grid = input.split('\n')
width = len(grid)
height = len(grid[0])

antennas = defaultdict(list)
for i in range(width):
    for j in range(height):
        cell = grid[i][j]
        if cell != '.':
            antennas[cell].append((i, j))

def compute_antinodes(a1, a2):
    i1, j1 = a1
    i2, j2 = a2
    di = i2-i1
    dj = j2-j1 
    return (i1-di, j1-dj), (i2+di, j2+dj)

def in_grid(a, width, height):
    i, j = a
    return 0 <= i < width and 0 <= j < height

antinodes = set()
for _, pos in antennas.items():
    for k in range(len(pos)):
        for l in range(k+1, len(pos)):
            a1, a2 = compute_antinodes(pos[k], pos[l])
            antinodes.add(a1)
            antinodes.add(a2)
            
impact = len([x for x in antinodes if in_grid(x, width, height)])
print(impact)


def compute_all_antinodes(a1, a2, width, height):
    i1, j1 = a1
    i2, j2 = a2
    di = i2-i1
    dj = j2-j1
    antinodes = set()
    k = 0
    while in_grid((a := (i1-k*di, j1-k*dj)), width, height):
        antinodes.add(a)
        k += 1
    k= 0
    while in_grid((a := (i2+k*di, j2+k*dj)), width, height):
        antinodes.add(a)
        k += 1
    return antinodes

antinodes = set()
for _, pos in antennas.items():
    for k in range(len(pos)):
        for l in range(k+1, len(pos)):
            new = compute_all_antinodes(pos[k], pos[l], width, height)
            antinodes = antinodes.union(new)

impact = len(antinodes)
print(impact)
