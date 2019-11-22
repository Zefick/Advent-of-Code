
from utils import Input, printResult

# https://adventofcode.com/2018/day/6

coords = list(map(lambda m: (int(m[1]), int(m[2])), \
    Input(2018, 6).match("(\\d+), (\\d+)")))

n = len(coords)
safepoints = 0
nearest = dict((i, 0) for i in range(n))
for i in range(500):
    for j in range(500):
        dsum = 0
        b = True
        minD, m = 2000, 0
        for k in range(n):
            d = abs(coords[k][0] - i) + abs(coords[k][1] - j)
            dsum += d
            if d == minD:
                b = False
            elif d < minD:
                minD = d
                m = k
                b = True
        if b and m in nearest:
            if i == 0 or i == 499 or j == 0 or j == 499:
                nearest.pop(m)
            else:
                nearest[m] += 1
        if dsum < 10000:
            safepoints += 1

printResult(1, max(nearest.values()))
printResult(2, safepoints)