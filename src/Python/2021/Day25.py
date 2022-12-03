
from utils import Input, printResult

# https://adventofcode.com/2021/day/25

input = Input(2021, 25).lines()

east = set()
south = set()
h, w = len(input), len(input[0])
for y in range(h):
    for x in range(w):
        if input[y][x] == '>':
            east.add((x, y))
        elif input[y][x] == 'v':
            south.add((x, y))

def print_map(east, south) :
    canvas = [['.'] * w for _ in range(h)]
    for (x, y) in east:
        canvas[y][x] = '>'
    for (x, y) in south:
        canvas[y][x] = 'v'
    print("\n".join("".join(canvas[i]) for i in range(h)), "\n")

stuck = False
for step in range(1000000):
    if stuck:
        break

    stuck = True
    nexts = set()
    for x, y in east:
        x2 = (x+1) % w
        if (x2, y) in east or (x2, y) in south:
            nexts.add((x, y))
        else:
            nexts.add((x2, y))
            stuck = False
    east = nexts
    
    nexts = set()
    for x, y in south:
        y2 = (y+1) % h
        if (x, y2) in east or (x, y2) in south:
            nexts.add((x, y))
        else:
            nexts.add((x, y2))
            stuck = False
    south = nexts

#print_map(east, south)

printResult(1, step)
