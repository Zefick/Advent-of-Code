
from utils import Input, printResult
from collections import Counter

# https://adventofcode.com/2021/day/5

input = Input(2021, 5).match("(\\d+),(\\d+) -> (\\d+),(\\d+)")
lines = list([int(s[1]), int(s[2]), int(s[3]), int(s[4])] for s in input)

points = Counter()
for (x1, y1, x2, y2) in lines:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[(x, y1)] += 1

printResult(1, sum(1 for x in points.values() if x > 1))

for (x1, y1, x2, y2) in lines:
    if abs(x1-x2) == abs(y1-y2):
        if y1 > y2:
            x1, x2, y1, y2 = x2, x1, y2, y1
        dx = 1 if x2 > x1 else -1
        for i in range(y2 - y1 + 1):
            points[(x1 + dx * i, y1 + i)] += 1

printResult(2, sum(1 for x in points.values() if x > 1))
