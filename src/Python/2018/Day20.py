
from utils import Input, printResult

# https://adventofcode.com/2018/day/20

def route(pt, path, steps, map):
    mySteps = 0
    myPoint = pt
    i = -1
    deltas = {"E": [1, 0], "W": [-1, 0], "N": [0, -1], "S": [0, 1]}
    while True:
        i += 1
        c = path[i]
        if c in deltas:
            myPoint = (myPoint[0] + deltas[c][0], myPoint[1] + deltas[c][1])
            mySteps += 1
            if myPoint not in map:
                map[myPoint] = steps + mySteps
        elif c == "(":
            i += route(myPoint, path[i+1:], steps + mySteps, map)
            continue
        elif c in [")", "$"]:
            return i + 1
        elif c == "|":
            myPoint = pt
            mySteps = 0

input = Input(2018, 20).lines()[0]
map = {}
route((0, 0), input, 0, map)

printResult(1, max(map.values()))
printResult(2, sum(1 for _ in filter(lambda x: x >= 1000, map.values())))
