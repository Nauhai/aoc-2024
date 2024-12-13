import sys
import re
from collections import namedtuple
import numpy as np

input = open(sys.argv[1], 'r').read().strip()
machines = input.split('\n\n')

Machine = namedtuple('Machine', ['xA', 'yA', 'xB', 'yB', 'X', 'Y'])

def parse_machine(machine_str):
    lines = machine_str.split('\n')
    m = re.search('Button A: X\+(\d+), Y\+(\d+)', lines[0])
    xA = int(m.group(1))
    yA = int(m.group(2))
    m = re.search('Button B: X\+(\d+), Y\+(\d+)', lines[1])
    xB = int(m.group(1))
    yB = int(m.group(2))
    m = re.search('Prize: X=(\d+), Y=(\d+)', lines[2])
    X = int(m.group(1))
    Y = int(m.group(2))
    return Machine(xA, yA, xB, yB, X, Y)

machines = [parse_machine(s) for s in machines]


def solve_system(machine):
    xA, yA, xB, yB, X, Y = machine
    return np.linalg.solve(np.array([[xA, xB], [yA, yB]]), np.array([X, Y]))

def is_solution(machine, A, B):
    xA, yA, xB, yB, X, Y = machine
    A = round(A)
    B = round(B)
    return A*xA + B*xB == X and A*yA + B*yB == Y 

def count_tokens(machines):
    tokens = 0
    for m in machines:
        A, B = solve_system(m)
        if is_solution(m, A, B):
            tokens += 3*A+B
    return round(tokens)

print(count_tokens(machines))

machines = [Machine(m.xA, m.yA, m.xB, m.yB, m.X+10000000000000, m.Y+10000000000000) for m in machines]
print(count_tokens(machines))

