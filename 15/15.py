import sys
import time
from copy import deepcopy

input = open(sys.argv[1], 'r').read().strip()
grid, moves = input.split('\n\n')
initial_grid = [[x for x in line] for line in grid.split('\n')]
moves = [m for line in moves.split('\n') for m in line]
width = len(initial_grid)
height = len(initial_grid[0])

for i in range(width):
    for j in range(height):
        if initial_grid[i][j] == '@':
            initial_pos = (i, j)
            initial_grid[i][j] = '.'

grid = deepcopy(initial_grid)
pos = initial_pos


def get_first_empty(grid, pos, dir):
    i, j = pos
    di, dj = dir
    i += di
    j += dj
    while grid[i][j] not in ('.', '#'):
        i += di
        j += dj
    if grid[i][j] == '#':
        return None
    return i, j

DIRS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

for move in moves:
    dir = DIRS[move]
    empty = get_first_empty(grid, pos, dir)
    if empty:
        i, j = pos
        di, dj = dir
        ei, ej = empty
        if grid[i+di][j+dj] == 'O':
            grid[ei][ej] = 'O'
        grid[i+di][j+dj] = '.'
        pos = (i+di, j+dj)

result = 0
for i in range(width):
    for j in range(height):
        if grid[i][j] == 'O':
            result += 100*i+j
print(result)


grid = []
for line in initial_grid:
    wide_line = []
    for x in line:
        if x == 'O':
            wide_line += ['[', ']']
        else:
            wide_line += [x]*2
    grid.append(wide_line)

width = width
height = height*2
i, j = initial_pos
pos = (i, j*2)

def can_push(grid, pos, dir):
    i, j = pos
    di, dj = dir

    if grid[i+di][j+dj] == '#':
        return False
    if grid[i+di][j+dj] == '.':
        return True
    
    # next cell is a crate

    if di == 0:
        return can_push(grid, (i, j+dj), dir)

    if grid[i+di][j] == '[':
        delta = 1
    else:
        delta = -1
    return can_push(grid, (i+di, j), dir) and can_push(grid, (i+di, j+delta), dir)

def push(grid, pos, dir):
    i, j = pos
    di, dj = dir

    if not can_push(grid, pos, dir):
        return

    if grid[i+di][j+dj] == '.':
        grid[i+di][j+dj] = grid[i][j]
        grid[i][j] = '.'
        return

    # next cell is crate
    
    if di == 0:
        push(grid, (i, j+dj), dir)
        grid[i][j+dj] = grid[i][j]
        grid[i][j] = '.'
        return

    if grid[i+di][j] == '[':
        delta = 1
    else:
        delta = -1

    push(grid, (i+di, j), dir)
    push(grid, (i+di, j+delta), dir)
    grid[i+di][j] = grid[i][j]
    grid[i][j] = '.'

for move in moves:
    dir = DIRS[move]
    if not can_push(grid, pos, dir):
        continue

    push(grid, pos, dir)
    i, j = pos
    di, dj = dir
    pos = (i+di, j+dj)

result = 0
for i in range(width):
    for j in range(height):
        if grid[i][j] == '[':
            result += 100*i+j
print(result)

