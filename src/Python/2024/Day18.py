
from utils import Input, printResult,neigthbors2d

# https://adventofcode.com/2024/day/18

input = Input(2024, 18).lines()

bytes = [tuple(map(int, s.split(","))) for s in input]
h, w = 71, 71

def display(positions):
    tiles = " ▀▄█"
    for y in range(0, h+1, 2):
        line = []
        for x in range(w):
            n = ((x, y) in positions) + ((x, y+1) in positions) * 2
            line.append(tiles[n])
        print("".join(line))

def findPath(n):
    visited = set()
    steps = set([(0, 0)])
    corrupted = set(bytes[:n])
    t = 0
    while steps:
        if (w-1, h-1) in steps:
            return t
        next_steps = set()
        for x, y in steps:
            for x2, y2 in neigthbors2d(x, y, False, limits=[0, w, 0, h]):
                if (x2, y2) not in corrupted and (x2, y2) not in visited:
                    visited.add((x2, y2))
                    next_steps.add((x2, y2))
        t += 1
        steps = next_steps
    return 0

printResult(1, findPath(1024))

l, r = 0, len(bytes)
while l < r:
    m = (l + r) // 2
    n = findPath(m)
    if n == 0:
        r = m
    else:
        l = m + 1

printResult(2, f"{input[l-1]} ({l})")
