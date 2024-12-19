import sys

input = open(sys.argv[1], 'r').read().strip()
towels, patterns = input.split('\n\n')
towels = towels.split(', ')
patterns = patterns.split('\n')


cache = dict()
def get_every_ways(pattern, towels):
    if pattern in cache:
        return cache[pattern]
    
    ways = 0
    for towel in towels:
        if pattern.startswith(towel):
            rest = pattern[len(towel):]

            if rest == '':
                ways += 1
            else:
                ways += get_every_ways(rest, towels)

    cache[pattern] = ways
    return ways

count_possibles = 0
count_ways = 0
for pattern in patterns:
    if (ways := get_every_ways(pattern, towels)):
        count_possibles += 1
        count_ways += ways

print(count_possibles, count_ways, sep='\n')

