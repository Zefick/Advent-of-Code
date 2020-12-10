
from utils import Input, printResult
from itertools import takewhile

# https://adventofcode.com/2020/day/9

input = list(map(int, Input(2020, 9).lines()))

n = len(input)
part1 = input[next(i for i in range(25, n) if all(input[x] + y != input[i] for x in range(i-25, i-1) for y in input[x+1:i]))]
part2 = next(x for x in (next(input[i:j] for j in range(i+1, n) if sum(input[i:j]) >= part1) for i in range(n)) if sum(x) == part1)
part2 = min(part2) + max(part2)

printResult(1, part1)
printResult(2, part2)
