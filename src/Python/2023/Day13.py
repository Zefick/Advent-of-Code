
from utils import Input, printResult

# https://adventofcode.com/2023/day/13

input = Input(2023, 13).lines()

def reflections(pattern, diff):
    n = len(pattern)
    w = len(pattern[0])
    for i in range(n-1):
        m = min(i+1, n-i-1)
        if sum(pattern[i-j][k] != pattern[i+j+1][k] for j in range(m) for k in range(w)) == diff:
            return i + 1
    return 0

res1, res2 = 0, 0
pattern = []
for line in input:
    if line:
        pattern.append(line)
    else:
        res1 += reflections(pattern, 0) * 100
        res2 += reflections(pattern, 1) * 100
        pattern = list(zip(*pattern))
        res1 += reflections(pattern, 0)
        res2 += reflections(pattern, 1)
        pattern = []

printResult(1, res1)
printResult(2, res2)
