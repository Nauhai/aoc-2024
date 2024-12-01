import sys
from collections import Counter

input = open(sys.argv[1], 'r').read().strip()
numbers = list(map(int, input.split()))
list1 = sorted(numbers[::2])
list2 = sorted(numbers[1::2])

diff = sum([abs(x-y) for (x, y) in zip(list1, list2)])
print(diff)

counter = Counter(list2)
score = sum([x*counter[x] for x in list1])
print(score)

