
from utils import Input, printResult
from functools import cache

# https://adventofcode.com/2024/day/19

input = Input(2024, 19).lines()
patterns = input[0].split(', ')
towels = input[2:]

@cache
def count_ways(target: str) -> int:
    if not target:
        return 1
    return sum(count_ways(target[len(w):]) \
        for w in patterns \
        if target.startswith(w))

towels = list(map(count_ways, towels))
printResult(1, sum(t > 0 for t in towels))
printResult(2, sum(towels))
