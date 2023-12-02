
from utils import Input, printResult

# https://adventofcode.com/2022/day/18

input = Input(2022, 18).lines()

lava = set(tuple(map(int, s.split(","))) for s in input)

dirs = [[0, 0, 1], [0, 0, -1],
        [0, 1, 0], [0, -1, 0],
        [1, 0, 0], [-1, 0, 0]]

faces = 0
for x, y, z in lava:
    faces += sum((x+dx, y+dy, z+dz) not in lava for dx, dy, dz in dirs)

printResult(1, faces)

minx, miny, minz = (min(c[i] for c in lava) for i in range(3))
maxx, maxy, maxz = (max(c[i] for c in lava) for i in range(3))

cur = set([(minx-1, miny-1, minz-1)])
visited = set()
faces = 0
while cur:
    next_wave = set()
    for x, y, z in cur:
        for dx, dy, dz in dirs:
            cube = (x2, y2, z2) = x+dx, y+dy, z+dz
            if not (minx-1 <= x2 <= maxx+1) or \
                    not (miny-1 <= y2 <= maxy+1) or \
                    not (minz-1 <= z2 <= maxz+1):
                continue
            if cube in lava:
                faces += 1
            elif cube not in visited:
                visited.add(cube)
                next_wave.add(cube)
    cur = next_wave
   
printResult(2, faces)
