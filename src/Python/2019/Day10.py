
import math
from utils import Input, printResult

# https://adventofcode.com/2019/day/10

asteroids = set()
input = Input(2019, 10).lines()
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == "#":
            asteroids.add((x, y))

def visibleFrom(point):
    result = []
    for b in asteroids:
        if b == point:
            continue
        steps = math.gcd(abs(point[0]-b[0]), abs(point[1]-b[1]))
        dy = (point[0] - b[0]) // steps
        dx = (point[1] - b[1]) // steps
        if not any((point[0] - dy*i, point[1] - dx*i) in asteroids for i in range(1, steps)):
            result.append(b)
    return result

visible = dict((a, len(visibleFrom(a))) for a in asteroids)
best = max(visible, key = visible.__getitem__)
           
printResult(1, visible[best])

queue = visibleFrom(best)
queue.sort(key = lambda x: (math.atan2(x[0] - best[0], best[1] - x[1])) % 7)
target = queue[199]
printResult(2, target[0] * 100 + target[1])

