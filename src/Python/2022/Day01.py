
from utils import Input

# https://adventofcode.com/2022/day/1

input = Input(2022, 1).lines()

s = 0
cals = []

for x in input:
    if x == "":
        cals.append(s)
        s = 0
    else:
        s += int(x)

cals = sorted(cals, reverse=True)

print("part1: ", cals[0])
print("part2: ", sum(cals[:3]))
