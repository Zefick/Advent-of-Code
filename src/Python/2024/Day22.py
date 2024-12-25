
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2024/day/22

input = Input(2024, 22).lines()

def next_secret(x):
    x = (x ^ (x << 6)) % 16777216
    x = (x ^ (x >> 5)) # % 16777216
    return (x ^ (x << 11)) % 16777216

all_changes = defaultdict(int)
    
part1 = 0
for i in range(len(input)):
    x = int(input[i])
    p = []
    changes = set()
    p.append(x % 10)
    for i in range(2000):
        x = next_secret(x)
        p.append(x % 10)
        if i > 4:
            p0, p1, p2, p3, p4 = p[-5:]
            c = (p1-p0, p2-p1, p3-p2, p4-p3)
            if c not in changes:
                changes.add(c)
                all_changes[c] += p4
    part1 += x

printResult(1, part1)
printResult(2, max(all_changes.values()))
