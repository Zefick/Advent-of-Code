
from utils import Input, printResult
import re, collections

# https://adventofcode.com/2021/day/22

input = Input(2021, 22).lines()

def parse_line(line):
    on = line[:2] == "on"
    x1, x2, y1, y2, z1, z2 = map(int, re.findall("-?\d+", line))
    return (x1, x2, y1, y2, z1, z2, on)

cubes = set()

for s in input:
    x1, x2, y1, y2, z1, z2, on = parse_line(s)
    x1 = max(x1, -50)
    x2 = min(x2, 50)
    y1 = max(y1, -50)
    y2 = min(y2, 50)
    z1 = max(z1, -50)
    z2 = min(z2, 50)
    for i in range(x1, x2+1):
        for j in range(y1, y2 + 1):
            for k in range(z1, z2 + 1) :
                if on and (i, j, k) not in cubes:
                    cubes.add((i, j, k))
                if not on and (i, j, k) in cubes:
                    cubes.remove((i, j, k))

printResult(1, len(cubes))

cubes = collections.Counter()
for line in input:
    x11, x12, y11, y12, z11, z12, on = parse_line(line)
    on = 1 if on else -1

    update = collections.Counter()
    for (x21, x22, y21, y22, z21, z22), on2 in cubes.items():
        ix0 = max(x11, x21); ix1 = min(x12, x22)
        iy0 = max(y11, y21); iy1 = min(y12, y22)
        iz0 = max(z11, z21); iz1 = min(z12, z22)
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= on2
    if on > 0:
        update[(x11, x12, y11, y12, z11, z12)] += on
    cubes.update(update)

v = sum((x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * n
          for (x1, x2, y1, y2, z1, z2), n in cubes.items())
printResult(2, v)
