
from utils import Input, printResult
import re
from math import floor

# https://adventofcode.com/2024/day/13

input = Input(2024, 13).lines()

n = len(input) // 4 + 1
machines = []
for i in range(n):
    m1 = re.search("X\+(\d+), Y\+(\d+)", input[i*4])
    m2 = re.search("X\+(\d+), Y\+(\d+)", input[i*4+1])
    m3 = re.search("X=(\d+), Y=(\d+)", input[i*4+2])
    machines.append(
        list(map(int, [m1.group(1), m1.group(2), m2.group(1), m2.group(2), m3.group(1), m3.group(2)])))
    
def solve(x1, y1, x2, y2, X, Y):
    # x1 * a + x2 * b = X 
    # y1 * a + y2 * b = Y
    p1 = X*y1 - Y*x1
    p2 = X*y2 - Y*x2
    q = y1*x2 - y2*x1
    if p1%q==0 and p2%q==0:
        return 3 * p2//-q + p1//q
    return 0

part1, part2 = 0, 0
for x1, y1, x2, y2, X, Y in machines:
    for a in range(100):
        for b in range(100):
            if a * x1 + b * x2 == X and a * y1 + b * y2 == Y:
                part1 += a * 3 + b

    part2 += solve(x1, y1, x2, y2, X + 10**13, Y + 10**13)

printResult(1, part1)
printResult(2, part2)
