
from utils import Input, printResult
import itertools

# https://adventofcode.com/2020/day/17

input = Input(2020, 17).lines()

# input = [
#     ".#.",
#     "..#",
#     "###"
# ]

def nearby3d(cell):
    x, y, z = cell
    res = set(itertools.product((x-1, x, x+1), (y-1, y, y+1), (z-1, z, z+1)))
    res.remove(cell)
    return res

def nearby4d(cell):
    x, y, z, w = cell
    res = set(itertools.product((x-1, x, x+1), (y-1, y, y+1), (z-1, z, z+1), (w-1, w, w+1)))
    res.remove(cell)
    return res

def play(start, dim):
    active = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '#':
                active.add((i, j, 0) if dim == 3 else (i, j, 0, 0))

    nearby = nearby3d if dim == 3 else nearby4d
    import time
    for n in range(6):
        t = time.time()
        cur_gen = {}
        for c in active:
            for c2 in nearby(c):
                cur_gen[c2] = cur_gen.get(c2, 0) + 1
        active = set(c for (c, m) in cur_gen.items() if m == 3 or (m == 2 and c in active))
        t = time.time() - t
    return active

printResult(1, len(play(input, 3)))
printResult(2, len(play(input, 4)))
