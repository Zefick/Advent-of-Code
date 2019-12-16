
import math
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/11

input = Input(2019, 11).lines()[0]

def runWith(code):
    queue = [code]
    if code == 1:
        queue = [1] + [0] * 1000000
    robot = Intcode(input, queue).run()
    field = {}
    p = (0, 0)
    d = 0
    dirs = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
    while True:
        color = next(robot, None)
        if color is None:
            break
        field[p] = color
        d = (d - 1 + next(robot) * 2) % 4
        p = (p[0] + dirs[d][0], p[1] + dirs[d][1])
        queue.append(field.get(p, 0))
    return field

field = runWith(0)
printResult(1, len(field))

field = runWith(1)
miny = min(p[0] for p in field)
maxy = max(p[0] for p in field)
minx = min(p[1] for p in field)
maxx = max(p[1] for p in field)

id = ""
palette = {0: "  ", 1: "@@"}
for y in range(miny, maxy+1):
    id  += "\n" + "".join(
        palette[field.get((y, x), 0)]
        for x in range(minx, maxx+1))

printResult(2, id)
