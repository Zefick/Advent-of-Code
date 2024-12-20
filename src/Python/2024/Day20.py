
from utils import Input, printResult
from collections import Counter

# https://adventofcode.com/2024/day/20

input = list(Input(2024, 20).lines())

h, w = len(input), len(input[0])

for y in range(h):
    for x in range(w):
        if input[y][x] == 'S':
            start = (y, x)

track = {start: 0}
steps = set([start])
t = 1
while steps:
    next_steps = set()
    for y, x in steps:
        for x2, y2 in [[x-1, y], [x, y-1], [x, y+1], [x+1, y]]:
            if input[y2][x2] != '#' and (y2, x2) not in track:
                track[(y2, x2)] = t
                next_steps.add((y2, x2))
    t += 1
    steps = next_steps

cnt1 = Counter()
cnt2 = Counter()
for y, x in track:
    for x2 in range(x-20, x+21):
        dx = abs(x2-x)
        for y2 in range(y-(20-dx), y+(21-dx)):
            if (y2, x2) in track:
                d = abs(x2-x) + abs(y2-y)
                cheat = track[(y, x)] - track[(y2, x2)] - d
                if cheat >= 100:
                    cnt2[cheat] += 1
                if d <= 2 and cheat >= 100:
                    cnt1[cheat] += 1

printResult(1, cnt1.total())
printResult(2, cnt2.total())
