
from utils import Input, printResult

# https://adventofcode.com/2022/day/9

input = list(Input(2022, 9).lines())

for p, k in [[1, 2], [2, 10]]:
    seen = set()
    knots = [[0, 0] for _ in range(k)]
    for s in input:
        d = s[0]
        n = int(s[2:])
        if d == 'R': dx, dy = 1, 0
        if d == 'L': dx, dy = -1, 0
        if d == 'U': dx, dy = 0, 1
        if d == 'D': dx, dy = 0, -1
        for _ in range(1, n+1):
            knots[0] = [knots[0][0] + dx, knots[0][1] + dy]
            for j in range(1, k):
                h = knots[j-1]
                t = knots[j]
                if abs(t[0] - h[0]) > 1 or abs(t[1] - h[1]) > 1:
                    if t[0] != h[0]:
                        t[0] = t[0] + (h[0] - t[0]) // abs(t[0] - h[0])
                    if t[1] != h[1]:
                        t[1] = t[1] + (h[1] - t[1]) // abs(t[1] - h[1])
                knots[j] = t
            seen.add(tuple(knots[-1]))
            
    printResult(p, len(seen))
