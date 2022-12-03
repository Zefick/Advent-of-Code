
from utils import printResult

# https://adventofcode.com/2021/day/23

# input = hardcoded

'''
This file represents the solution when each state encode as a string of constant length
Positive feature of this approach is that we don't need to calculate state's hash by hand anymore
Rooms and hall information are easier to get as well as for the "class" version of the solution
'''

prices = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
dests = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
stashes = [1, 11, 2, 10, 4, 6, 8]

def findmoves(state, points, L) :
    result = []
    top = [None] * 4
    hall = state[:11]
    rooms = state[11:]
    occupied = [i+1 for i in range(11) if hall[i] != '.']

    for i in range(4):
        for j in range(L):
            if rooms[i*L+j] != '.':
                top[i] = j + 1
                break

    # move to the home room
    for x in range(1, 12):
        c = hall[x-1]
        if c == '.':
            continue

        dest = dests[c]
        i = (dest - 3) // 2
        
        # too early
        if top[i] and rooms[i*L+top[i]-1] != '*':
            continue

        # blocked by someone in the hallway
        if any((x2 - dest) * (x2 - x) < 0 for x2 in occupied):
            continue

        newy = top[i] - 1 if top[i] else L
        newpos = list(state)
        newpos[x-1] = '.'
        newpos[10 + i*L + newy] = '*'
        pts = prices[c] * (abs(x-dest) + newy)
        result.append(("".join(newpos), points + pts))
    
    if result:
        # force this moves
        return result

    # move from a room
    for i in range(4):
        if not top[i]:
            continue
        y = top[i]
        x = i * 2 + 3
        c = rooms[i*L+y-1]

        # already good destination room
        if c == '*':
            continue

        for s in stashes:
            # blocked by someone in the hallway
            if any((x2 - x) * (x2 - s) <= 0 for x2 in occupied):
                continue
            newpos = list(state)
            newpos[s-1] = c
            newpos[10 + i*L + y] = '.'
            pts = prices[c] * ((abs(x - s) + y))
            result.append(("".join(newpos), points + pts))

    return result

import heapq

def solve(start, finish, L) :
    stack = [(0, start)]
    cache = {}
    best = 10 ** 10
    while stack:
        pts, pos = heapq.heappop(stack)
        moves = findmoves(pos, pts, L)
        for pos2, pts2 in moves:
            if pts2 >= best:
                continue
            if pos2 == finish:
                if (pts2 < best):
                    print(pts2)
                    best = pts2
            else:
                if pos2 not in cache or cache[pos2] > pts2:
                    cache[pos2] = pts2
                    heapq.heappush(stack, (pts2, pos2))
    print("cache len: " + str(len(cache)))
    return best

start =  "...........BDAABDCC"
finish = "...........********"

from time import time
t = time()
printResult(1, solve(start, finish, 2))
print(time() - t)

start =  "...........BDDDACBABBADCACC"
finish = "...........****************"

t = time()
printResult(2, solve(start, finish, 4))
print(time() - t)
