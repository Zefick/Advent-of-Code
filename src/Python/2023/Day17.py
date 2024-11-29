
from utils import Input, printResult
from bisect import insort_right
from collections import deque

# https://adventofcode.com/2023/day/17

input = [list(map(int, line)) for line in Input(2023, 17).lines()]

h, w = len(input), len(input[0])
dirs = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
turns = {'>': ('v', '^'), '<': ('v', '^'), 'v': ('<', '>'), '^':('<', '>')}

def next_states_1(y, x, d, k):
    res = []
    if k < 3:
        res.append((y, x, d, k+1))
    res.append((y, x, turns[d][0], 1))
    res.append((y, x, turns[d][1], 1))
    return res

# lost heat, y, x, direction, straigth steps
def find_path(next_states):
    q = deque([(0, 0, 0, '>', 1), (0, 0, 0, 'v', 1)])
    seen = {}
    while q:
        heat, y, x, d, k = q.popleft()
        dy, dx = dirs[d]
        x, y = x + dx, y + dy
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        heat += input[y][x]
        if seen.get((y, x, d, k), 10000) <= heat:
            continue
        seen[(y, x, d, k)] = heat
        for (y, x, d, k) in next_states(y, x, d, k):
            insort_right(q, (heat, y, x, d, k))
    return seen

import time
t = time.time() 
seen = find_path(next_states_1)

m = min(ht for (y, x, _, k), ht in seen.items() if x == w-1 and y == h-1)
printResult(1, m)

def next_states_2(y, x, d, k):
    res = []
    if k < 10:
        res.append((y, x, d, k+1))
    if k > 3:
        res.append((y, x, turns[d][0], 1))
        res.append((y, x, turns[d][1], 1))
    return res

print(time.time() - t, "\n")
t = time.time()

seen = find_path(next_states_2)

m = min(ht for (y, x, _, k), ht in seen.items() if x == w-1 and y == h-1 and k > 3)
printResult(2, m)

print(time.time() - t)
