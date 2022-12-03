
from collections import defaultdict
from utils import Input, printResult

# https://adventofcode.com/2021/day/14

input = Input(2021, 14).lines()

polimer = input[0]
insertions = {}

for s in input[2:]:
    s = s.split(" -> ")
    insertions[s[0]] = s[1]

pairs = defaultdict(lambda: 0)
for i in range(len(polimer) - 1):
    pairs[polimer[i:i+2]] += 1

for i in range(40):
    p2 = defaultdict(lambda: 0)
    for p, n in pairs.items():
        if p in insertions:
            r = insertions[p]
            p2[p[0] + r] += pairs[p]
            p2[r + p[1]] += pairs[p]
    pairs = p2

    if i in [9, 39]:
        times = defaultdict(lambda: 0)
        for p, n in pairs.items():
            times[p[0]] += n
        times[polimer[-1]] += 1
        ans = max(times.values()) - min(times.values())
        printResult(1 if i == 9 else 2, ans)
