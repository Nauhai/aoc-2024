import sys
import re

input = open(sys.argv[1], 'r').read().strip()

matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', input)
result = sum([int(m.group(1))*int(m.group(2)) for m in matches])
print(result)

matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", input)
result = 0
enabled = True

for match in matches:
    if match.group(0) == "do()":
        enabled = True
    elif match.group(0) == "don't()":
        enabled = False
    else:
        if enabled:
            result += int(match.group(1))*int(match.group(2))

print(result)
