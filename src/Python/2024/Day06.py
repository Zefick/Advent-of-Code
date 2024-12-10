
from utils import Input, printResult
from itertools import product

# https://adventofcode.com/2024/day/6

input = list(map(list, Input(2024, 6).lines()))

h, w = len(input), len(input[0])
for (y, x) in product(range(h), range(w)):
    if input[y][x] == '^':
        start = (y, x)
        break

(y, x), dx, dy = start, 0, -1
part1 = set([start])
while 0 <= y+dy < h and 0 <= x+dx < w:
    if input[y+dy][x+dx] == '#':
        dx, dy = -dy, dx
    else:
        y, x = y + dy, x + dx
        part1.add((y, x))

printResult(1, len(part1))

def find_loop(guard, dy, dx):
    y, x = guard
    trace = set()
    while 0 <= y+dy < h and 0 <= x+dx < w:
        if ((y, x), dx, dy) in trace:
            return True
        trace.add(((y, x), dx, dy))
        if input[y+dy][x+dx] == '#':
            dx, dy = -dy, dx
        else:
            y, x = y + dy, x + dx
    return False

part2 = set()
for (y, x) in part1:
    if (y, x) != start and input[y][x] != '#':
        input[y][x] = '#'
        if find_loop(start, -1, 0):
            part2.add((y, x))
        input[y][x] = '.'

printResult(2, len(part2))
