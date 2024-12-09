import sys
from collections import deque, namedtuple

input = open(sys.argv[1], 'r').read().strip()
blocks = [None]*sum(list(map(int, input)))
free_space = deque() 

id = 0
file = True
i = 0
j = 0
while j < len(input):
    end = i+int(input[j])
    if file:
        while i < end:
            blocks[i] = id
            i += 1
        id += 1
    else:
        while i < end:
            free_space.append(i)
            i += 1
    file = not file
    j += 1

while len(free_space) > 0:
    while ((id := blocks.pop()) is None):
        continue
    pos = free_space.popleft()
    if pos >= len(blocks):
        blocks.append(id)
        break
    blocks[pos] = id

checksum = sum([i*id for (i, id) in enumerate(blocks)])
print(checksum)


Block = namedtuple('Block', ['pos', 'len'])
file_blocks = dict()
free_space = [] 

i = 0
j = 0
file = True
id = 0
while j < len(input):
    l = int(input[j])
    if l > 0:
        if file:
            file_blocks[id] = Block(i, l)
            id += 1
        else:
            free_space.append(Block(i, l))
        i += l
    j += 1
    file = not file

id -= 1
while id >= 0:
    block = file_blocks[id]
    for i, free in enumerate(free_space):
        if free.pos >= block.pos:
            break
        if free.len >= block.len:
            file_blocks[id] = Block(free.pos, block.len)
            if free.len > block.len:
                free_space[i] = Block(free.pos+block.len, free.len-block.len)
            else:
                del free_space[i]
            break
    id -= 1

checksum = 0
for id, block in file_blocks.items():
    for i in range(block.pos, block.pos+block.len):
        checksum += id*i
print(checksum)

