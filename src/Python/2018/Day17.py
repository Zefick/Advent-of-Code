
from utils import Input, printResult
import re

# https://adventofcode.com/2018/day/17

clay = set()
for m in Input(2018, 17).match("(.)=(\\d+), .=(\\d+)..(\\d+)"):
    x, a, b = int(m[2]), int(m[3]), int(m[4])
    for y in range(a, b+1):
        clay.add((x, y) if m[1] == "x" else (y, x))

miny = min(p[1] for p in clay)
maxy = max(p[1] for p in clay)

flow = set([(500, miny)])
water = set()
wet = set(flow)
while len(flow) > 0:
    nextFlow = set()
    for drop in flow:
        wet.add(drop)
        p = (drop[0], drop[1] + 1)
        if p not in clay and p not in water:
            if p[1] <= maxy:
                nextFlow.add(p)
            continue

        left = (drop[0] - 1, drop[1])
        while left not in clay:
            p = (left[0], drop[1] + 1)
            if p in clay or p in water:
                wet.add(left)
                left = (left[0] - 1, left[1])
            else:
                nextFlow.add(left)
                left = None
                break

        right = (drop[0] + 1, drop[1])
        while right not in clay:
            p = (right[0], drop[1] + 1)
            if p in clay or p in water:
                wet.add(right)
                right = (right[0] + 1, right[1])
            else:
                nextFlow.add(right)
                right = None
                break

        if left and right:
            water.update((x, drop[1]) for x in range(left[0]+1, right[0]))
            nextFlow.add((drop[0], drop[1]-1))

    flow = nextFlow

printResult(1, len(wet))
printResult(2, len(water))
