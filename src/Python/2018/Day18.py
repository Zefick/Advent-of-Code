
from utils import Input, printResult
import copy

# https://adventofcode.com/2018/day/18

field = list(map(list, Input(2018, 18).lines()))
states = [".", "|", "#"]
h, w = len(field), len(field[0]) - 1
m = 1000
scores = [0] * m
for t in range(m):
    field2 = copy.deepcopy(field)
    for y in range(h):
        for x in range(w):
            counts = [0, 0, 0]
            for dir in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                p = [x + dir[0], y + dir[1]]
                if p[0] >= 0 and p[0] < w and p[1] >= 0 and p[1] < h:
                    counts[states.index(field2[p[1]][p[0]])] += 1
            if field2[y][x] == '.' and counts[1] >= 3: field[y][x] = "|"
            if field2[y][x] == '|' and counts[2] >= 3: field[y][x] = "#"
            if field2[y][x] == '#' and (counts[1] == 0 or counts[2] == 0): field[y][x] = "."
    counts = [
        sum(line.count("|") for line in field),
        sum(line.count("#") for line in field)
    ]
    scores[t] = counts[0] * counts[1]

printResult(1, scores[9])

for t in range(m-2, 1, -1):
    if scores[t] == scores[m-1]:
        period = m - 1 - t
        printResult(2, scores[m + 1000_000_000 % period - m % period - period - 1])
        break
