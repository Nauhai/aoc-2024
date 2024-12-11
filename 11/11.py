import sys
import functools

input = open(sys.argv[1], 'r').read().strip()
stones = [int(x) for x in input.split(' ')]

@functools.cache
def compute(stone, n):
    if n == 0:
        return 1

    if stone == 0:
        return compute(1, n-1)

    if len((s := str(stone)))%2 == 0:
        left = int(s[:len(s)//2])
        right = int(s[len(s)//2:])
        return compute(left, n-1) + compute(right, n-1)

    return compute(stone*2024, n-1)

def run(stones, n):
    result = 0
    for stone in stones:
        result += compute(stone, n)
    return result

print(run(stones, 25))
print(run(stones, 75))

