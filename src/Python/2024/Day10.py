
from utils import Input, printResult, neigthbors2d
from itertools import product

# https://adventofcode.com/2024/day/10

input = [list(map(int, line)) for line in Input(2024, 10).lines()]

h, w = len(input), len(input[0])

def find_trails(x, y, k, trails):
    if input[y][x] == 9:
        trails.add((x, y))
        return 1
    res = 0
    for y2, x2 in neigthbors2d(y, x, False, limits=[0, h, 0, w]):
        if input[y2][x2] == k + 1:
            res += find_trails(x2, y2, k+1, trails)
    return res

part1, part2 = 0, 0
for (y, x) in product(range(h), range(w)):
    if input[y][x] == 0:
        trails = set()
        part2 += find_trails(x, y, 0, trails)
        part1 += len(trails)

printResult(1, part1)
printResult(2, part2)
