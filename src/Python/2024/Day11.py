
from utils import Input, printResult
from collections import Counter

# https://adventofcode.com/2024/day/11

input = list(map(int, (Input(2024, 11).lines()[0].split())))

def split(x):
    s = str(x)
    if len(s) % 2 == 0:
        m = len(s) // 2
        return [int(s[:m]), int(s[m:])]
    else:
        return [1] if x == 0 else [x * 2024]

def simulate(steps):
    cnt = Counter(input)
    for _ in range(steps):
        next_cnt = Counter()
        for x, n in cnt.items():
            for s in split(x):
                next_cnt[s] += n
        cnt = next_cnt
    return cnt.total()

printResult(1, simulate(25))
printResult(2, simulate(75))
