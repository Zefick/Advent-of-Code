
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/24

input = Input(2020, 24).lines()

dirs = {'nw': [0, 1], 'ne': [1, 1], 'e': [1, 0], 'se': [0, -1], 'sw': [-1, -1], 'w': [-1, 0]}

def decode(line):
    steps = re.findall("(e|se|sw|w|nw|ne)", line)
    pos = [0, 0]
    for s in steps:
        pos[0] += dirs[s][0]
        pos[1] += dirs[s][1]
    return tuple(pos)

tiles = set()
for line in input:
    pos = decode(line)
    if pos in tiles: tiles.remove(pos)
    else: tiles.add(pos)

printResult(1, len(tiles))

def adj(pos):
    x, y = pos
    return ((x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1))

def isBlack(t, tiles):
    n = sum(1 for x in adj(t) if x in tiles)
    return n == 2 or (t in tiles) and n == 1

for i in range(100):
    process = set()
    for t in tiles:
        process |= set(adj(t))
        process.add(t)
    tiles = set(filter(lambda t: isBlack(t, tiles), process))

printResult(2, len(tiles))
