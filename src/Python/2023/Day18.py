
from utils import Input, printResult

# https://adventofcode.com/2023/day/18

input = list(Input(2023, 18).match("(.) (\d+) \(#(.{5})(.)\)"))

# Shoelace Formula
def find_square(input):
    x, y, s = 0, 0, 0
    for dir, n in input:
        x2, y2 = x, y
        if dir == 'R': x2 += n
        if dir == 'D': y2 += n
        if dir == 'L': x2 -= n 
        if dir == 'U': y2 -= n
        s += (x * y2 - y * x2) + n
        x, y = x2, y2
    return s // 2 + 1

input1 = [(s[1], int(s[2])) for s in input]
printResult(1, find_square(input1))

input2 = [("RDLU"[int(s[4])], int(s[3], base=16)) for s in input]
printResult(2, find_square(input2))
