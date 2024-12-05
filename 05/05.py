import sys
from functools import cmp_to_key, partial


input = open(sys.argv[1], 'r').read().strip()
split = input.split('\n\n')
rules = set(tuple(map(int, x.split('|'))) for x in split[0].split())
updates = [list(map(int, x.split(','))) for x in split[1].split()]

def is_correct(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rules:
               return False
    return True

score = 0
for update in updates:
    if is_correct(update):
        score += update[len(update)//2]

print(score)


def cmp(x, y, rules):
    return -1 if (x, y) in rules else 1

score = 0
for update in updates:
    if not is_correct(update):
        corrected = sorted(update, key=cmp_to_key(partial(cmp, rules=rules)))
        score += corrected[len(corrected)//2]

print(score)
