
from utils import Input, printResult

# https://adventofcode.com/2018/day/2

lines = sorted(Input(2018, 2).lines())
a, b = 0, 0
for line in lines:
    if any(line.count(c) == 2 for c in line): a += 1
    if any(line.count(c) == 3 for c in line): b += 1
printResult(1, a * b)

for (a, b) in zip(lines[:-2], lines[1:]):
    for i in range(len(a)):
        if a[:i] + a[i+1:] == b[:i] + b[i+1:]:
            printResult(2, a[:i] + a[i+1:])
