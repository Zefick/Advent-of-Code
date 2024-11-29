
from utils import Input, printResult

# https://adventofcode.com/2023/day/16

input = Input(2023, 16).lines()

h, w = len(input), len(input[0])

def bean(x, y, dx, dy):
    seen = set()
    energized = set()
    q = [(x, y, dx, dy)]
    while q:
        x, y, dx, dy = q.pop()
        if (x, y, dx, dy) in seen:
            continue
        seen.add((x, y, dx, dy))
        energized.add((x, y))
        x += dx
        y += dy
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        c = input[y][x]
        if c == '.' or (c == '-' and dy == 0) or (c == '|' and dx == 0):
            q.append((x, y, dx, dy))
        elif c == '|':
            q.append((x, y, 0, -1))
            q.append((x, y, 0, 1))
        elif c == '-':
            q.append((x, y, -1, 0))
            q.append((x, y, 1, 0))
        elif c == '/':
            dx, dy = -dy, -dx
            q.append((x, y, dx, dy))
        elif c == '\\':
            dx, dy = dy ,dx
            q.append((x, y, dx, dy))
    return len(energized) - 1

printResult(1, bean(-1, 0, 1, 0))

m1 = max(max((bean(x, -1, 0, 1), bean(x, h, 0, -1))) for x in range(w))
m2 = max(max((bean(-1, y, 1, 0), bean(-1, y, 1, 0))) for y in range(h))

printResult(2, max(m1, m2))
