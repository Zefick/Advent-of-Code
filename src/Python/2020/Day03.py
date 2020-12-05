
from utils import Input, printResult

# https://adventofcode.com/2020/day/3

input = Input(2020, 3).lines()

m = [0] * 5
for y, line in enumerate(input):
    m[0] += line[y % len(line)] == '#'
    m[1] += line[(y * 3) % len(line)] == '#'
    m[2] += line[(y * 5) % len(line)] == '#'
    m[3] += line[(y * 7) % len(line)] == '#'
    m[4] += y%2 == 0 and line[y//2 % len(line)] == '#'

printResult(1, m[1])
printResult(2, m[0] * m[1] * m[2] * m[3] * m[4])
