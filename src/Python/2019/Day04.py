
from utils import printResult

# https://adventofcode.com/2019/day/4

cnt1, cnt2 = 0, 0
for s in map(str, range(137683, 596253 + 1)):
    if all(s[i+1] >= s[i] for i in range(5)):
        if any(s.count(c) >= 2 for c in s): cnt1 += 1
        if any(s.count(c) == 2 for c in s): cnt2 += 1

printResult(1, cnt1)
printResult(2, cnt2)
