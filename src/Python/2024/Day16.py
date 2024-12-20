
from utils import Input, printResult
from collections import deque

# https://adventofcode.com/2024/day/16

input = Input(2024, 16).lines()

h, w = len(input), len(input[0])

for y in range(h):
    for x in range(w):
        if input[y][x] == 'S':
            start = (y, x)
        elif input[y][x] == 'E':
            end = (y, x)

q = deque([(start[0], start[1], 0, 1, 0)])
visited = {}
best = float('inf')
while q:
    y, x, dy, dx, pts = q.popleft()
    if (y, x) == end:
        if pts < best:
            best = pts
    elif (y, x, dy, dx) not in visited or visited[(y, x, dy, dx)] > pts:
        visited[(y, x, dy, dx)] = pts
        if input[y+dy][x+dx] != '#':
            q.append((y+dy, x+dx, dy, dx, pts+1))
        q.append((y, x, -dx, dy, pts+1000))
        q.append((y, x, dx, -dy, pts+1000))

printResult(1, best)

# backtracking from finish to start
part2 = set()
q = [(end[0], end[1], 0, 1, best), (end[0], end[1], 1, 0, best),
     (end[0], end[1], 0, -1, best), (end[0], end[1], -1, 0, best)]
while q:
    y, x, dy, dx, pts = q.pop()
    if (y-dy, x-dx, dy, dx) in visited and visited[(y-dy, x-dx, dy, dx)] == pts-1:
        part2.add((y, x))
        q.append((y-dy, x-dx, dy, dx, pts-1))
        # optimization to not process the same node twice
        visited[(y-dy, x-dx, dy, dx)] = 0

    for dy, dx in [(-dx, dy), (dx, -dy)]:
        if (y, x, dy, dx) in visited and visited[(y, x, dy, dx)] == pts-1000:
            q.append((y, x, dy, dx, pts-1000))

printResult(2, len(part2) + 1)
