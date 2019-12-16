
import math
from utils import Input, printResult
import copy

# https://adventofcode.com/2019/day/12

coords = [[1, -4, 3], [-14, 9, -4], [-4, -6, 7], [6, -9, -11]]
velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def calcCoords(coords, velocity, k):
    for i, j in [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]:
        sign = int((coords[i][k] > coords[j][k]) - (coords[i][k] < coords[j][k]))
        velocity[i][k] -= sign
        velocity[j][k] += sign

    for i in range(4):
        coords[i][k] += velocity[i][k]

for _ in range(1000):
    for k in range(3):
        calcCoords(coords, velocity, k)

printResult(1, sum(sum(map(abs, coords[i])) * sum(map(abs, velocity[i])) for i in range(4)))

import time
t = time.time()

coords0 = copy.deepcopy(coords)
velocity0 = copy.deepcopy(velocity)

periods = []
for k in range(3):
    for p in range(1, 10**10):
        calcCoords(coords, velocity, k)
        if coords == coords0 and velocity == velocity0:
            periods.append(p)
            break

lcm = periods[0] * periods[1] // math.gcd(periods[0], periods[1])
lcm *= periods[2] // math.gcd(lcm, periods[2])

printResult(2, lcm)

print("time: %.2fs" % (time.time() - t))

