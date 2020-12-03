
import math
from utils import Input, printResult
from collections import deque, namedtuple, defaultdict

# https://adventofcode.com/2019/day/20

input = Input(2019, 20).lines()

portals = defaultdict(list)
def addPortal(name, enter, outer):
    portals[name].append((enter, outer))

H = len(input)
for y in range(1, H-1):
    W = len(input[y])
    for x in range(1, W-1):
        if input[y][x] == '.':
            if input[y-1][x].isupper():
                addPortal(input[y-2][x] + input[y-1][x], (x, y), y == 2 or y == H-3)
            if input[y+1][x].isupper():
                addPortal(input[y+1][x] + input[y+2][x], (x, y), y == 2 or y == H-3)
            if input[y][x-1].isupper():
                addPortal(input[y][x-2:x], (x, y), x == 2 or x == W-3)
            if input[y][x+1].isupper():
                addPortal(input[y][x+1:x+3], (x, y), x == 2 or x == W-3)

portals2 = {}
start = portals["AA"][0][0]
end = portals["ZZ"][0][0]
for p in portals.values():
    if len(p) == 1:
        # start and end portals loop to themselves
        portals2[p[0][0]] = (p[0][0], 0)
    if len(p) == 2:
        portals2[p[0][0]] = (p[1][0], -1 if p[0][1] else 1)
        portals2[p[1][0]] = (p[0][0], -1 if p[1][1] else 1)
portals = portals2

def findPortals(start):
    paths = []
    visited = set()
    Q = deque([(start, 0)])
    while Q:
        pt, d = Q.popleft()
        if pt in visited or input[pt[1]][pt[0]] != '.':
            continue
        visited.add(pt)
        if pt in portals:
            paths.append((*portals[pt], d+1))
        for p in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            Q.append(((pt[0] + p[0], pt[1] + p[1]), d+1))
    return paths

paths = dict((p, findPortals(p)) for p in portals)
    
def run(recursive):
    best = 100000
    visited = {}
    State = namedtuple('State', ['pt', 'z', 'd'])
    Q = [State(start, 0, 0)]
    while Q[0].d < best:
        Q.sort(key = lambda s: s.d)
        S = Q.pop(0)
        hash = (S.pt, S.z)
        if S.z < 0 or (hash in visited and visited[hash] <= S.d):
            continue
        visited[hash] = S.d
        if S.pt == end and (S.z == 0 or not recursive) and S.d < best:
            best = S.d
        for p in paths[S.pt]:
            Q.append(State(p[0], S.z + p[1], S.d + p[2]))
    return best

import time
t = time.time()

printResult(1, run(False) - 1)
printResult(2, run(True) - 1)

print(time.time() - t)
