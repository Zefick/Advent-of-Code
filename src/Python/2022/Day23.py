
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2022/day/23

input = Input(2022, 23).lines()

elves = set()
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            elves.add((i, j))

def print_map(elves):
    minx = min(e[1] for e in elves)
    maxx = max(e[1] for e in elves)
    miny = min(e[0] for e in elves)
    maxy = max(e[0] for e in elves)
    for y in range(miny, maxy+1):
        s = ['.'] * (maxx - minx + 2)
        for x in range(maxx - minx + 2):
            if (y, x+minx) in elves:
                s[x] = '#'
        print("".join(s))

import time
t = time.time()

for round in range(10000):
    concurrent_cells = defaultdict(int)
    prepared_elves = []
    next_elves = set()
    for y, x in elves:
        nbs = [(y2, x2) in elves for (x2, y2) in 
               [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1],
                [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]]
        if not any(nbs):
            next_elves.add((y, x))
        else:
            wanted = None
            for j in range(4):
                d = (round + j) % 4
                if d == 0:
                    if not (nbs[0] | nbs[3] | nbs[5]):
                        wanted = (y-1, x)
                        break
                elif d == 1:
                    if not (nbs[2] | nbs[4] | nbs[7]):
                        wanted = (y+1, x)
                        break
                elif d == 2:
                    if not (nbs[0] | nbs[1] |nbs[2]):
                        wanted = (y, x-1)
                        break
                elif d == 3:
                    if not (nbs[5] | nbs[6] | nbs[7]):
                        wanted = (y, x+1)
                        break
            if wanted:
                prepared_elves.append((x, y, wanted[1], wanted[0]))
                concurrent_cells[wanted] += 1
            else:
                next_elves.add((y, x))
    n = 0
    for x, y, x2, y2 in prepared_elves:
        if concurrent_cells[(y2, x2)] < 2:
            next_elves.add((y2, x2))
            n += 1
        else:
            next_elves.add((y, x))
    elves = next_elves

    if (round == 9):
        minx = min(e[1] for e in elves)
        maxx = max(e[1] for e in elves)
        miny = min(e[0] for e in elves)
        maxy = max(e[0] for e in elves)
        printResult(1, (maxx-minx+1) * (maxy-miny+1) - len(elves))

    if n == 0:
        break
    
# print_map(elves)
printResult(2, round + 1)

print(time.time() - t)
