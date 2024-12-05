
from utils import Input, printResult
from itertools import product

# https://adventofcode.com/2024/day/4

input = Input(2024, 4).lines()

h, w = len(input), len(input[0])

part1 = 0
for y, x in product(range(h), range(w)):
    for (dy, dx) in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        if 0 <= y+dy*3 < h and 0 <= x+dx*3 < w:
            part1 += all(input[y+dy*i][x+dx*i] == "XMAS"[i] for i in range(4))

printResult(1, part1)

part2 = 0
for y, x in product(range(1, h-1), range(1, w-1)):
    if input[y][x] == 'A' and \
            input[y-1][x-1] + input[y+1][x+1] in ["MS", "SM"] and \
            input[y+1][x-1] + input[y-1][x+1] in ["MS", "SM"]:
        part2 += 1

printResult(2, part2)
