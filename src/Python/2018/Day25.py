
from utils import Input, printResult
import time

# https://adventofcode.com/2018/day/25

def distance(star1, star2):
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])\
         + abs(star1[2] - star2[2]) + abs(star1[3] - star2[3])

tm = time.time()
groups = []
for line in Input(2018, 25).lines():
    star = tuple(map(int, line.split(",")))
    group = None
    for g in groups[:]:
        if any(distance(star, s) <= 3 for s in g):
            if group is None:
                g.append(star)
                group = g
            else:
                group += g
                groups.remove(g)
    if group is None:
        groups.append([star])

print(len(groups))
print("time: %.2f sec" % (time.time() - tm))
