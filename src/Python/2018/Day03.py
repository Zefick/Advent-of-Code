
from utils import Input, printResult
import re

# https://adventofcode.com/2018/day/3

lines = Input(2018, 3).match("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)")
peaces = [list(map(int, [m[1], m[2], m[3], m[4], m[5]])) for m in lines]

fabric = [[0] * 1000 for _ in range(1000)]
for (_, x, y, w, h) in peaces:
    for a in range(x, x+w):
        for b in range(y, y+h):
            fabric[a][b] += 1

printResult(1, sum(x > 1 for f in fabric for x in f))

for (id, x, y, w, h) in peaces:
    if not any(any(v > 1 \
            for v in fabric[a][y:y+h]) \
            for a in range(x, x+w)):
        printResult(2, id)
