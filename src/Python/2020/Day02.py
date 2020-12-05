
from utils import Input, printResult

# https://adventofcode.com/2020/day/2

input = Input(2020, 2).match("(\d+)-(\d+) (\w):\s*(.*)")

part1, part2 = 0, 0
for m in input:
    a, b, c, s = int(m[1]), int(m[2]), m[3], m[4]
    n = s.count(c)
    if n >= a and n <= b:
        part1 += 1
    if (s[a-1] == c) ^ (s[b-1] == c):
        part2 += 1

printResult(1, part1)
printResult(2, part2)
