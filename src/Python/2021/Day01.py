
from utils import Input

# https://adventofcode.com/2021/day/1

input = list(map(int, Input(2021, 1).lines()))

print("part1: ", sum(map(int.__lt__, input, input[1:])))
print("part2: ", sum(map(int.__lt__, input, input[3:])))
