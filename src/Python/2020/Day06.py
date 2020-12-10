
from utils import Input, printResult
from functools import reduce

# https://adventofcode.com/2020/day/6

input = Input(2020, 6).lines()
input.append("")

def getGroups(input):
    group = []
    for line in input:
        if len(line) == 0:
            yield group
            group = []
        else:
            group.append(line)

part1, part2 = 0, 0
for group in getGroups(input):
    ans = list(map(set, group))
    part1 += len(reduce(set.union, ans))
    part2 += len(reduce(set.intersection, ans))

printResult(1, part1)
printResult(2, part2)
