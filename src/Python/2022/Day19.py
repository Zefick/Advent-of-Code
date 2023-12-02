
from utils import Input, printResult
from functools import cache

# https://adventofcode.com/2022/day/19

input = Input(2022, 19).match(".*(\d+):.*?(\d+) .*?(\d+) .*?(\d+) .*?(\d+) .*?(\d+) .*?(\d+) ")

blueprints = []
for m in input:
    m = list(int(m[i]) for i in range(2, 8))
    blueprints.append(((m[0], 0, 0, 0), (m[1], 0, 0, 0), \
                       (m[2], m[3], 0, 0), (m[4], 0, m[5], 0)))
    
def is_dominated(ores1, ores2, robots1, robots2):
    # if ores2[3] > ores1[3]:
    #     return True
    return ores1 is not ores2 and \
            all(ores1[i] <= ores2[i] for i in range(4)) and \
            all(robots1[i] <= robots2[i] for i in range(4))

'''
The first optimization idea is to reduce the number of variants in the search tree by limiting the amount of stored ore
and limiting number of robots of first three types by maximum robot price because 
we can build only one robot at a time, and the additional ore collected by extra robots will simply be wasted.
Since we know the prices of all the robots, there is no point in storing too much ore too, it just bloats the number of variants.

The next optimization is to remove dominanted variants for each cycle.
A variant is considered dominated if there is another variant with the same or more ore and robots of each type.
'''
def bfs(bp, max_time):
    maxprices = [max(price[i] for price in bp) for i in range(4)]
    maxprices[3] = 1000
    cur_cycle = [((0, 0, 0, 0), (1, 0, 0, 0))]
    for t in range(max_time - 1):
        next_cycle = set()
        for ores, robots in cur_cycle:
            next_cycle.add((tuple(min(ores[i] + robots[i], maxprices[i] * 2) for i in range(4)), robots))
            for r in range(4):      
                # try build a robot
                if r == 3 or maxprices[r] > robots[r]:
                    if all(ores[i] >= bp[r][i] for i in range(3)):
                        next_cycle.add((tuple(min(ores[i] - bp[r][i] + robots[i], maxprices[i] * 2) for i in range(4)), \
                                        tuple(robots[i] + (i == r) for i in range(4))))
        # removing dominated variants
        cur_cycle = []
        for ores, robots in next_cycle:
            if not any(is_dominated(ores, ores2, robots, robots2) for ores2, robots2 in next_cycle):
                cur_cycle.append((ores, robots))
        # if t > 24:
        #     print(t, len(cur_cycle))
    return max(ore[3] + robots[3] for ore, robots in cur_cycle)

import time
t = time.time()

res = 0
n = len(blueprints)
for i in range(n):
    m = bfs(blueprints[i], 24)
    res += (i+1) * m

printResult(1, res)

g1 = bfs(blueprints[0], 32)
g2 = bfs(blueprints[1], 32)
g3 = bfs(blueprints[2], 32)

printResult(2, g1 * g2 * g3)

print(f"time: {time.time() - t:.3f}")
