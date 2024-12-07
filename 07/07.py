import sys
from itertools import product 

input = open(sys.argv[1], 'r').read().strip()
lines = [line.split(': ') for line in input.split('\n')]
lines = [(int(result), list(map(int, rest.split()))) for result, rest in lines]

def compute(values, operators):
    total = values[0]
    for i in range(1, len(values)):
        match operators[i-1]:
            case '+':
                total += values[i]
            case '*':
                total *= values[i]
            case '||':
                total = int(str(total) + str(values[i]))
    return total

def is_solvable(result, values, operators):
    op_comb = product(*([operators]*(len(values)-1)))
    for comb in op_comb:
        if compute(values, comb) == result:
            return True
    return False

def solve(lines, operators):
    score = 0
    for result, values in lines:
        if is_solvable(result, values, operators):
            score += result
    return score

print(solve(lines, ['+', '*']))
print(solve(lines, ['+', '*', '||']))

