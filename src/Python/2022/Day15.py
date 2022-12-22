
from utils import Input, printResult

# https://adventofcode.com/2022/day/15

input = Input(2022, 15).match(".* x=(-?\d+), y=(-?\d+): .* x=(-?\d+), y=(-?\d+)")

sonar = []
for m in input:
    sx, sy, bx, by = int(m[1]), int(m[2]), int(m[3]), int(m[4])
    sonar.append([sx, sy, abs(sx-bx) + abs(sy-by)])
    
sonar = list(map(tuple, sorted(sonar, key=(lambda x: x[2]), reverse=True)))

# if we assume that free space is continuoes we can make it easier
# but we don't sure

def merge(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
    result = []
    for x in intervals:
        if not result or x[0] > result[-1][1]:
            result.append(x)
        else:
            result[-1][1] = max(x[1], result[-1][1])
    return result

y = 2_000_000
intervals = []
for sx, sy, r in sonar:
    if (h := r - abs(sy-y)) > 0:
        intervals.append([sx - h, sx + h])
        intervals = merge(intervals)

printResult(1, sum(x2 - x1 for x1, x2 in intervals))

def scan(y):
    x = 0
    while x < 4_000_000:
        for sx, sy, r in sonar:
            if r > abs(sx-x) + abs(sy-y):
                x2 = sx + r - abs(sy-y) + 1
                if x2 > x:
                    x = x2
                    break
        else:
            break
    return x

for y in range(0, 4_000_000):
    # if y % 100000 == 0:
    #     print(y)
    if (x := scan(y)) < 4_000_000:
        printResult(2, x * 4_000_000 + y)
        break
