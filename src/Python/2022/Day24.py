
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2022/day/24

input = Input(2022, 24).lines()

# input = [
#     "#.######",
#     "#>>.<^<#",
#     "#.<..<<#",
#     "#>v.><>#",
#     "#<^v^^>#",
#     "######.#"
# ]

blizzards = set()
h, w = len(input), len(input[0])

for i in range(1, h-1):
    for j in range(1, w-1):
        if input[i][j] != '.':
            blizzards.add((i, j, input[i][j]))


def print_blizzards(blizzards):
    for i in range(1, h-1):
        line = ['.'] * (w-2)
        for y, x, d in blizzards:
            if y == i:
                if line[x-1] == '.':
                    line[x-1] = d
                else:
                    line[x-1] = '2' if line[x-1] in '<>v^' else str(int(line[x-1]) + 1)
        print("".join(line))
    print()


def next_blizzards(blizzards):
    new_blizzards = set()
    for y, x, d in blizzards:
        if d == '>':
            x = (1 if x == w-2 else x+1)
        elif d == '<':
            x = (w-2 if x == 1 else x-1)
        if d == 'v':
            y = (1 if y == h-2 else y+1)
        elif d == '^':
            y = (h-2 if y == 1 else y-1)
        new_blizzards.add((y, x, d))
    return new_blizzards

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def find_way(src, dst, blizzards):
    cur = [src]
    steps = 0
    while True:
        next_steps = set()
        bz = set((y, x) for y, x, _ in blizzards)
        for y, x in cur:
            if (y, x) not in bz:
                next_steps.add((y, x))
            for dy, dx in dirs:
                x2, y2 = x + dx, y + dy
                if (y2, x2) == dst:
                    return steps, blizzards
                if (y2, x2) not in bz and (0 < x2 < w-1) and (0 < y2 < h-1):
                    next_steps.add((y2, x2))
        steps += 1
        cur = next_steps
        blizzards = next_blizzards(blizzards)

steps1, blizzards = find_way((0, 1), (h-1, w-2), blizzards)
printResult(1, steps1)

steps2, blizzards = find_way((h-1, w-2), (0, 1), blizzards)
steps3, blizzards = find_way((0, 1), (h-1, w-2), blizzards)
printResult(2, steps1 + steps2 + steps3)
