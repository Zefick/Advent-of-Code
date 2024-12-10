
from utils import Input, printResult
from itertools import product, combinations
from collections import defaultdict

# https://adventofcode.com/2024/day/8

input = Input(2024, 8).lines()

h, w = len(input), len(input[0])
nodes = defaultdict(list)
for (y, x) in product(range(h), range(w)):
    if input[y][x] != '.':
        nodes[input[y][x]].append((y, x))

antinodes = set()
for vals in nodes.values():
    for (y1, x1), (y2, x2) in combinations(vals, 2):
        dx, dy = x2-x1, y2-y1
        antinode = (y1-dy, x1-dx)
        if 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinodes.add(antinode)
        antinode = (y2+dy, x2+dx)
        if 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinodes.add(antinode)
printResult(1, len(antinodes))

antinodes = set()
for vals in nodes.values():
    for (y1, x1), (y2, x2) in combinations(vals, 2):
        dx, dy = x2-x1, y2-y1
        antinode = (y1, x1)
        while 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinodes.add(antinode)
            antinode = (antinode[0] - dy, antinode[1] - dx)
        antinode = (y2, x2)
        while 0 <= antinode[0] < h and 0 <= antinode[1] < w:
            antinodes.add(antinode)
            antinode = (antinode[0] + dy, antinode[1] + dx)
printResult(2, len(antinodes))
