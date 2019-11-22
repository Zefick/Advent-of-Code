
from utils import Input, printResult

# https://adventofcode.com/2018/day/11

def getPower(x, y, serial):
    id = x + 10
    return (((id * y + serial) * id) // 100) % 10 - 5

serial = 3613
stripes = []
for i in range(300):
    stripes.append([[] for _ in range(300)])
    for j in range(300):
        power = 0
        for s in range(min(30, 300-j)):
            power += getPower(i+1, j+s+1, serial)
            stripes[i][j].append(power)

def findMax(s1, s2):
    maxPower = 0
    maxx, maxy, maxs = 0, 0, 0
    for size in range(s1, s2+1):
        for i in range(301-size):
            for j in range(301-size):
                power = sum(stripes[i+s][j][size-1] for s in range(size))
                if maxPower < power:
                    maxPower, maxx, maxy, maxs = power, i, j, size
    return (maxx+1, maxy+1, maxs, maxPower)

part1 = findMax(3, 3)
printResult(1, "(%d,%d) %d" % (part1[0], part1[1], part1[2]))
part2 = findMax(1, 30)
printResult(2, "(%d,%d,%d) %d" % part2)
