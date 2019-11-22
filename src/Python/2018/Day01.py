
import itertools
from utils import Input, printResult

# https://adventofcode.com/2018/day/1

nums = list(map(int, Input(2018, 1).lines()))
printResult(1, sum(nums))

visited, s = set([0]), 0
for x in itertools.cycle(nums):
    s += x
    if s in visited:
        printResult(2, s)
        break
    visited.add(s)
