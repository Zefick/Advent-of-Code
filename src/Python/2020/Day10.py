
from utils import Input, printResult

# https://adventofcode.com/2020/day/10

input = [0] + sorted(list(map(int, Input(2020, 10).lines())))

diffs = [0, 0, 1]
for i in range(len(input)-1):
    diffs[input[i+1] - input[i] - 1] += 1

printResult(1, diffs[0] * diffs[2])

seen = {}
def ways(start, adapters):
    if start in seen:
        return seen[start]
    n = 0
    for k in range(start+1, start+4):
        if k in adapters:
            n += ways(k, adapters)
    n += (n == 0)
    seen[start] = n
    return n

printResult(2, ways(0, set(input)))
