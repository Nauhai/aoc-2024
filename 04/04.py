import sys
from collections import Counter

input = open(sys.argv[1], 'r').read().strip()
grid = input.split('\n')
l, c = len(grid), len(grid[0])

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def search_word(word, grid, i, j, di, dj):
    l = len(grid)
    c = len(grid[0])

    for k in range(len(word)):
        if not (0 <= i+k*di < l and 0 <= j+k*dj < c):
            return False
        if grid[i+k*di][j+k*dj] != word[k]:
            return False 
    return True
                
count = 0
for i in range(l):
    for j in range(c):
        if grid[i][j] != 'X':
            continue

        for (di, dj) in dirs:
            if search_word('XMAS', grid, i, j, di, dj):
                count += 1

print(count)


dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
count = 0
middles = []
for i in range(l):
    for j in range(c):
        if grid[i][j] != 'M':
            continue

        for di, dj in dirs:
            if search_word('MAS', grid, i, j, di, dj):
                middles.append((i+di, j+dj))

counter = Counter(middles)
count = sum([c//2 for m, c in counter.items() if c%2 == 0])
print(count)

