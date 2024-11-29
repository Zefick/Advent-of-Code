
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2023/day/22

from itertools import groupby

input = Input(2023, 22).lines()

bricks = []
for line in input:
    start, end = line.split('~')
    start, end = start.split(','), end.split(',')
    x1, y1, z1 = list(map(int, start))
    x2, y2, z2 = list(map(int, end))
    block = []
    if x1 != x2:
        block = [(x, y1, z1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif y1 != y2:
        block = [(x1, y, z1) for y in range(min(y1, y2), max(y1, y2) + 1)]
    else:
        block = [(x1, y1, z) for z in range(min(z1, z2), max(z1, z2) + 1)]
    bricks.append(block)
    
bricks.sort(key=lambda b: b[0][2])

landed_blocks = {}
falling = []
for i, b in enumerate(bricks):
    if b[0][2] == 1:
        for (x, y, z) in b:
            landed_blocks[(x, y, z)] = i
    else:
        falling.append(i)

while falling:
    while True:
        stop = []
        next_falling = []
        for i in falling:
            fall = all(z != 1 and (x, y, z - 1) not in landed_blocks for x, y, z in bricks[i])
            if fall:
                next_falling.append(i)
            else:
                stop.append(i)
                for b in bricks[i]:
                    landed_blocks[b] = i
        falling = next_falling
        if not stop:
            break
    for i in falling:
        bricks[i] = [(x, y, z-1) for (x, y, z) in bricks[i]]

above = defaultdict(set)
below = defaultdict(set)
for i, b in enumerate(bricks):
    for x, y, z in bricks[i]:
        if (x, y, z+1) in landed_blocks:
            j = landed_blocks[(x, y, z+1)]
            if i != j:
                below[j].add(i)
                above[i].add(j)

part1 = sum(all(len(below[j]) > 1 for j in above[i]) for i in range(len(bricks)))
printResult(1, part1)

res = 0
for i in range(len(bricks)):
    q = set(above[i])
    falling = set([i])
    while q:
        next_q = set()
        for j in q:
            if all(k in falling for k in below[j]):
                falling.add(j)
                next_q |= above[j]
        q = next_q
    res += len(falling) - 1
                
printResult(2, res)
