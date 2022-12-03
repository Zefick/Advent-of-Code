
from utils import printResult

# https://adventofcode.com/2021/day/21

input = (3, 7)

die = 0
scores = [0, 0]
positions = [input[0], input[1]]

i = 0
while max(scores) < 1000:
    positions[i] = (positions[i] + die * 3 + 6) % 10
    scores[i] += positions[i] + 1
    die += 3
    i = 1 - i

printResult(1, min(scores) * die)

import time
t = time.time()

wins = [0, 0]
outcomes = {((0, 0), input) : 1}
die = [1, 3, 6, 7, 6, 3, 1]
i = 0
k = 0
while len(outcomes) > 0:
    new_outs = {}
    for vec, n in outcomes.items():
        s, p = vec
        for d in range(3, 10):
            n1 = die[d-3]
            p_new = (p[0] + d) % 10
            s_new = s[0] + p_new + 1
            if s_new >= 21:
                wins[i] += n * n1
            else:
                vec2 = ((s[1], s_new), (p[1], p_new))
                new_outs[vec2] = new_outs.get(vec2, 0) + n * n1
    i = 1 - i
    outcomes = new_outs
    k += 1
    print(k, len(outcomes))

printResult(2, max(wins))
print(time.time() - t)
