import sys
import re
from collections import namedtuple

input = open(sys.argv[1], 'r').read().strip()
WIDTH = 101 if len(sys.argv) < 3 else int(sys.argv[2]) 
HEIGHT = 103 if len (sys.argv) < 4 else int(sys.argv[3]) 


class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self):
        self.px += self.vx
        self.px %= WIDTH
        self.py += self.vy
        self.py %= HEIGHT

    def __repr__(self):
        return f'Robot({self.px}, {self.py}, {self.vx}, {self.vy})'

robots = []
for match in re.finditer('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', input):
    robots.append(Robot(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
    

for i in range(100):
    for robot in robots:
        robot.move()

quadrants = [0, 0, 0, 0]

for robot in robots:
    if robot.px < WIDTH//2:
        if robot.py < HEIGHT//2:
            quadrants[0] += 1
        elif robot.py > HEIGHT//2:
            quadrants[1] += 1
    elif robot.px > WIDTH//2:
        if robot.py < HEIGHT//2:
            quadrants[2] += 1
        elif robot.py > HEIGHT//2:
            quadrants[3] += 1

score = 1
for q in quadrants:
    score *= q
print(score)


def robots_to_positions(robots):
    positions = set()
    for robot in robots:
        positions.add((robot.px, robot.py))
    return positions

def print_grid(positions):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in positions:
                print('#', end='')
            else:
                print(' ', end='')
        print()

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def count_neighbors(positions):
    n = 0
    for x, y in positions:
        n += sum([(x+dx, y+dy) in positions for dx, dy in DIRS])
    return n

moves = 100 
while True: 
    for robot in robots:
        robot.move()
    moves += 1

    positions = robots_to_positions(robots)
    neighbors = count_neighbors(positions)

    if neighbors < 500:
        continue

    print('===== MOVE', moves, '=====')
    print_grid(positions)

