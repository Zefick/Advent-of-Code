
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2023/day/21

input = Input(2023, 21).lines()

h, w = len(input), len(input[0])
start = (65, 65)

def neigthbors2d(y: int, x: int, limits=None):
    dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for dy, dx in dirs:
        y2, x2 = y + dy, x + dx
        if limits is None or (limits[0] <= y2 < limits[1] and limits[2] <= x2 < limits[3]):
            yield(y2, x2)

nbs = defaultdict(list)
dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
for i in range(h):
    for j in range(w):
        for dy, dx in dirs:
            if input[(i+dy)%h][(j+dx)%w] != '#':
                nbs[(i, j)].append((dy, dx))

def brute_force(k):
    q = set([start])
    prev = set()
    n1, n2 = 1, 0
    for i in range(k):
        next_steps = set()
        for y, x in q:
            for dy, dx in nbs[(y%h, x%w)]:
                y2, x2 = y + dy, x + dx
                if (y2, x2) not in prev and input[y2%h][x2%w] != '#':
                    next_steps.add((y2, x2))
        prev = q
        q = next_steps
        n1, n2 = n2 + len(q), n1
    return n1

printResult(1, brute_force(64))

# PART II

'''
26501365 = 202300 * 131 + 65
reference = [3832, 33967, 94056, 184099, 304096, 454047, 633952]

y = Ax^2 + Bx + C

y(0) = C
y(1) = A + B + C
y(2) = 4A + 2B + C

2A = (y2 - C) - (y1 - C) * 2 => A = (y2 + C) / 2 - y1
B = y1 - C - A
'''

C = brute_force(65)
y1 = brute_force(131 + 65)
y2 = brute_force(131 * 2 + 65)
A = (y2 + C) // 2 - y1
B = y1 - C - A
x = 202300
printResult(2, A * x * x + B * x + C)
