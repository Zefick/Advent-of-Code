
from utils import Input, printResult
import bisect

# https://adventofcode.com/2023/day/11

input = Input(2023, 11).lines()

galaxies = []
h, w = len(input), len(input[0])
for i in range(h):
    for j in range(w):
        if input[i][j] == '#':
            galaxies.append((i, j))
            
n = len(galaxies)
dist, gaps = 0, 0

for axis, m in [[0, h], [1, w]]:
    coords = sorted(g[axis] for g in galaxies)
    dist += sum(x * (i*2 - n + 1) for i, x in enumerate(coords))
    for i in set(range(h)).difference(set(coords)):
        i = bisect.bisect_left(coords, i)
        gaps += i * (n-i)

printResult(1, dist + gaps)
printResult(2, dist + gaps * 999999)
