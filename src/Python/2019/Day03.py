
from utils import Input, printResult

# https://adventofcode.com/2019/day/3

input = Input(2019, 3).lines()

def getPath(input):
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    path = {}
    p, s = (0, 0), 0
    for segment in input:
        delta = dirs[segment[0]]
        for i in range(int(segment[1:])):
            s += 1
            p = (p[0] + delta[0], p[1] + delta[1])
            path[p] = s
    return path

from time import time
t = time()

path1 = getPath(input[0].split(","))
path2 = getPath(input[1].split(","))
print(len(path1), len(path2))

intersections = list(filter(lambda p: p in path1, path2))

printResult(1, min(abs(p[0]) + abs(p[1]) for p in intersections))
printResult(2, min(path1[p] + path2[p] for p in intersections))

print(time() - t)
