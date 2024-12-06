import sys
from collections import defaultdict

input = open(sys.argv[1], 'r').read().strip()
grid = input.split('\n')
width = len(grid)
height = len(grid[0])

class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    @classmethod
    def from_grid(cls, grid):
        width = len(grid)
        height = len(grid[0])

        obstacles = set()
        for i in range(width):
            for j in range(height):
                if grid[i][j] == '#':
                    obstacles.add((i, j))

        return cls(width, height, obstacles) 

    def is_valid(self, pos):
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def look_ahead(self, pos, dir):
        new_pos = (pos[0]+dir[0], pos[1]+dir[1])
        return new_pos in self.obstacles

    def add_obstacle(self, obstacle):
        return Grid(self.width, self.height, self.obstacles.union({obstacle})) 

visited = set()
starting_pos = (0, 0)
for i in range(width):
    if '^' in grid[i]:
        starting = (i, grid[i].index('^'))
        break;
starting_dir = (-1, 0)

grid = Grid.from_grid(grid)

def move(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])

def turn(dir):
    match dir:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)

def run(grid, starting_pos, starting_dir):
    pos = starting_pos
    dir = starting_dir 

    path = defaultdict(list)
    path[pos].append(dir)
    while True:
        if grid.look_ahead(pos, dir):
            dir = turn(dir)
        else:
            pos = move(pos, dir)
            if not grid.is_valid(pos):
                return path, False
            if dir in path[pos]:
                return path, True
            path[pos].append(dir)

path, _ = run(grid, starting, (-1, 0))
print(len(path))


loops = 0
for cell in path:
    new_grid = grid.add_obstacle(cell)
    path, loop = run(new_grid, starting, (-1, 0))
    if loop:
        loops += 1

print(loops)

