
import collections
from utils import Input, printResult

# https://adventofcode.com/2019/day/18

def reachablekeys(grid, start, havekeys):
    Q = collections.deque([start])
    distance = {start: 0}
    keys = {}
    while Q:
        h = Q.popleft()
        for (y, x, steps) in ngs[h]:
            p = (y, x)
            ch = grid[y][x]
            d = distance[h] + steps
            if (p in distance and distance[p] <= d) or (ch.isupper() and ch.lower() not in havekeys):
                continue
            distance[p] = d
            if ch.islower() and ch not in havekeys:
                keys[ch] = d, p
            else:
                Q.append(p)
    return keys

def reachable4(grid, starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in reachablekeys(grid, start, havekeys).items():
            keys[ch] = dist, pt, i
    return keys

def minwalk(grid, starts, havekeys):
    hks = ''.join(sorted(havekeys))
    if (starts, hks) in seen:
        return seen[starts, hks]
    keys = reachable4(grid, starts, havekeys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, i) in keys.items():
            nstarts = tuple(pt if i == j else p for j, p in enumerate(starts))
            poss.append(dist + minwalk(grid, nstarts, havekeys + ch))
        ans = min(poss)
    seen[starts, hks] = ans
    return ans

def buildNeigthbours(grid) :
    # build full map first
    ngs = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '#':
                ngs[(y,x)] = []
                for (x2, y2) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if grid[y2][x2] != '#':
                        ngs[(y, x)].append((y2, x2))
    # then reduce corridors
    min_ngs = {}
    for (y, x), arr in ngs.items():
        if len(arr) > 2 or grid[y][x].isalpha() or grid[y][x] == '@':
            res = []
            for (y1, x1) in arr:
                step = 1
                xPrev, yPrev = x, y
                while grid[y1][x1] == '.' and len(ngs[(y1, x1)]) == 2:
                    step += 1
                    if ngs[(y1, x1)][0] == (yPrev, xPrev):
                        yPrev, xPrev = y1, x1
                        y1, x1 = ngs[(y1, x1)][1]
                    else:
                        yPrev, xPrev = y1, x1
                        y1, x1 = ngs[(y1, x1)][0]
                if grid[y1][x1] != '.' or len(ngs[(y1, x1)]) > 1:
                    res.append((y1, x1, step))
            min_ngs[(y, x)] = res
    return min_ngs

grid = list(map(list, Input(2019, 18).lines()))
seen = {}
ngs = buildNeigthbours(grid)
printResult(1, minwalk(grid, ((40, 40),), ''))

grid[39][39:42] = "@#@"
grid[40][39:42] = "###"
grid[41][39:42] = "@#@"
ngs = buildNeigthbours(grid)
seen = {}
printResult(2, minwalk(grid, ((39, 39), (39, 41), (41, 39), (41, 41)), ''))
