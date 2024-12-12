import sys

input = open(sys.argv[1], 'r').read().strip()
grid = input.split('\n')
width = len(grid)
height = len(grid[0])


DIRS = dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_region(grid, width, height, i, j, current):
    t = grid[i][j]
    new = set()
    for (di, dj) in DIRS:
        if 0 <= i+di < width and 0 <= j+dj < height:
            if grid[i+di][j+dj] == t and (i+di, j+dj) not in current:
                current.add((i+di, j+dj))
                new = new.union(find_region(grid, width, height, i+di, j+dj, current))
                current = current.union(new)
    return current 

visited = set()
regions = []
for i in range(width):
    for j in range(height):
        if (i, j) in visited:
            continue
        current = set()
        current.add((i, j))
        region = find_region(grid, width, height, i, j, current)
        regions.append(region)
        visited = visited.union(region)

def perimeter(region):
    perimeter = 0
    for i, j in region:
        neighbors = 0
        for (di, dj) in DIRS:
            if (i+di, j+dj) in region:
                neighbors += 1
        perimeter += 4-neighbors
    return perimeter

price = 0
for region in regions:
    price += len(region)*perimeter(region)
print(price)

