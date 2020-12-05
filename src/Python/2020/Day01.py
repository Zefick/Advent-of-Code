
from utils import Input, printResult

# https://adventofcode.com/2020/day/1

input = list(map(int, Input(2020, 1).lines()))

for x in range(len(input)):
    for y in range(x+1, len(input)):
        a, b = input[x], input[y]
        if a + b == 2020:
            part1 = a * b
        elif a + b < 2020 and (2020 - a - b) in input[y+1:]:
            part2 = a * b * (2020 - a - b)

printResult(1, part1)
printResult(2, part2)
