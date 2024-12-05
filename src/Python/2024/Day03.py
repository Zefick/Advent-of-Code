
from utils import Input, printResult, neigthbors2d
import re

# https://adventofcode.com/2024/day/3

input = "".join(Input(2024, 3).lines())

part1 = 0
part2 = 0
do = True
match = re.finditer('(do\(\)|don\'t\(\))|(mul\((\d+),(\d+)\))', input)
for m in match:
    if m[1]:
        do = m[1] == "do()"
    if m[2]:
        mul = int(m[3]) * int(m[4])
        part1 += mul
        if do:
            part2 += mul

printResult(1, part1)
printResult(2, part2)
