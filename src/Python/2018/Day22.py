
from utils import Input, printResult

# https://adventofcode.com/2018/day/22

depth = 9171
target = (7, 721)

# {point: level} dict
map = {}

def getLevel(p: (int, int)) -> int:
    if p in map: return map[p]
    if p[0] == 0: level = p[1] * 48271
    elif p[1] == 0: level = p[0] * 16807
    else: level = getLevel((p[0], p[1]-1)) * getLevel((p[0]-1, p[1]))
    level = (level + depth) % 20183
    map[p] = level
    return level

distances = [{}, {}, {}]

def getDistance(p, tool) -> int:
    return distances[tool].get(p, 1000000)

def putDistance(p, tool, d):
    distances[tool][p] = d

risk = sum(getLevel((j, i)) % 3 for j in range(target[0] + 1) for i in range(target[1] + 1))
printResult(1, risk)

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = [((0, 0), 1, 0)]  # (x, y), tool, time

import time as tm
starttime = tm.time()

def checkCell(p, tool, time) :
    if time < getDistance(p, tool):
        putDistance(p, tool, time)
        queue.append((p, tool, time))

besttime = 1000000

for k in range(5000000):
    if len(queue) == 0:
        break
    p, tool, time = queue.pop(0)
    # current time not better than already found
    if time > getDistance(p, tool) or time >= besttime:
        continue
    if p == target:
        besttime = min(time if tool == 1 else time + 7, besttime)
        putDistance(p, 1, besttime)
        continue
    # check adjacent cells with a current tool
    for [dx, dy] in dirs:
        p2 = (p[0] + dx, p[1] + dy)
        if p2[0] < 0 or p2[1] < 0 or p2[0] > 100 or getLevel(p2) % 3 == tool:
            continue
        checkCell(p2, tool, time + 1)
    # change a tool
    checkCell(p, 3 - (tool + getLevel(p) % 3), time + 7)

printResult(2, getDistance(target, 1))

print("Finished after %d steps and %.2f sec." % (k, tm.time() - starttime))
