import sys

input = open(sys.argv[1]).read().strip()
reports = [list(map(int, l.split())) for l in input.split("\n")]

def is_safe(report):
    diffs = [report[i]-report[i+1] for i in range(len(report)-1)]
    return (all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs))) and all(map(lambda x: abs(x) <= 3, diffs))

safes = sum(map(is_safe, reports))
print(safes)

def is_safe_dampened(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False

safes_dampened = sum(map(is_safe_dampened, reports))
print(safes_dampened)

