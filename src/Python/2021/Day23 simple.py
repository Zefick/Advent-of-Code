
from utils import printResult
import itertools

# https://adventofcode.com/2021/day/23

# input = hardcoded

'''
Simple initial approach where state is represented by list of agents with three properties:
its type, x and y position in the cave
'''

prices = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
dests = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
stashes = [1, 11, 2, 10, 4, 6, 8]

q1, q2 = 0, 0

def findmoves(start, points, L) :
    global q1, q2

    result = []
    top = {}
    hall = list(filter(lambda amp: amp[2] == 0, start))
    rooms = list(filter(lambda amp: amp[2] != 0, start))
    occupied = [amp[1] for amp in hall]

    for amp in rooms:
        c, x, y = amp
        if x not in top or top[x][2] > y:
            top[x] = amp

    # move to the home
    for amp in set(top.values()) | set(hall):
        c, x, y = amp
        dest = dests[c]

        # already good destination room
        if x == dests[c] and all(c2 == c for c2, x2, y2 in rooms if (x2 == x and y2 > y)):
            continue

        # too early
        if not all(c2 == c for c2, x2, _ in rooms if x2 == dest):
            continue

        # blocked by someone in the hallway
        if any((x2 - dest) * (x2 - x) < 0 for x2 in occupied):
            continue

        newy = top[dest][2]-1 if dest in top else L
        newpos = start.copy()
        newpos.remove(amp)
        newpos.append((c, dest, newy))
        pts = prices[c] * (abs(x-dest) + newy + y)
        result.append((newpos, points + pts))
        q2 += 1
    
    if result:
        # force this moves
        return result

    # move from a room
    for amp in top.values():
        c, x, y = amp
        # already good destination room
        if x == dests[c] and all(c2 == c for c2, x2, y2 in rooms if (x2 == x and y2 > y)):
            continue
        for s in stashes:
            # blocked by someone in the hallway
            if any((x2 - x) * (x2 - s) <= 0 for x2 in occupied):
                continue
            newpos = start.copy()
            newpos.remove(amp)
            newpos.append((c, s, 0))
            pts = prices[c] * ((abs(x - s) + y))
            result.append((newpos, points + pts))
            q1 += 1

    return result

def hach_pos(start) :
    hash = ""
    for c, x, y in sorted(start):
        hash += c + str(x*10 + y)
    return hash
    
def hach_pos2(start) :
    hash = ["."] * (11 + len(start))
    for c, x, y in start:
        if y == 0:
            hash[x-1] = c
        else:
            hash[11 + (y-1)*4 + (x - 3) // 2] = c
    return "".join(hash)

import heapq

def solve(start, finish, L) :
    stack = [(0, start)]
    cache = {}
    best = 10 ** 10
    global q1, q2
    q1, q2 = 0, 0
    while stack:
        pts, pos = heapq.heappop(stack)
        moves = findmoves(pos, pts, L)
        for pos2, pts2 in moves:
            if pts2 >= best:
                continue
            if set(pos2) == finish:
                if (pts2 < best):
                    print(pts2)
                    best = pts2
            else:
                hash = hach_pos(pos2)
                if hash not in cache or cache[hash] > pts2:
                    cache[hash] = pts2
                    heapq.heappush(stack, (pts2, pos2))
    print("cache len: " + str(len(cache)))
    print("counters: ", str(q1), str(q2))
    return best

start = [('B', 3, 1), ('A', 5, 1), ('B', 7, 1), ('C', 9, 1), 
         ('D', 3, 2), ('C', 5, 2), ('B', 7, 2), ('A', 9, 2), 
         ('D', 3, 3), ('B', 5, 3), ('A', 7, 3), ('C', 9, 3), 
         ('D', 3, 4), ('A', 5, 4), ('D', 7, 4), ('C', 9, 4)]

finish = set([('A', 3, 1), ('B', 5, 1), ('C', 7, 1), ('D', 9, 1), 
              ('A', 3, 2), ('B', 5, 2), ('C', 7, 2), ('D', 9, 2), 
              ('A', 3, 3), ('B', 5, 3), ('C', 7, 3), ('D', 9, 3), 
              ('A', 3, 4), ('B', 5, 4), ('C', 7, 4), ('D', 9, 4)])

start1 = list(filter(lambda x: x[2] not in [2, 3], start))
start1 = list([(c, x, 1 if y == 1 else 2) for (c, x, y) in start1])
finish1 = list(filter(lambda x: x[2] not in [2, 3], finish))
finish1 = set([(c, x, 1 if y == 1 else 2) for (c, x, y) in finish1])

from time import time
t = time()
printResult(1, solve(start1, finish1, 2))
print(time() - t)

t = time()
printResult(2, solve(start, finish, 4))
print(time() - t)
