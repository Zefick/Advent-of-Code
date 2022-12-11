
from utils import Input, printResult

# https://adventofcode.com/2021/day/4

input = list(Input(2022, 4).match("(\d+)-(\d+),(\d+)-(\d+)"))

n1, n2 = 0, 0
for m in input:
    a, b, c, d = int(m[1]), int(m[2]), int(m[3]), int(m[4])
    n1 += (a <= c and b >= d) or (a >= c and b <= d)
    n2 += max(a, c) <= min(b, d)
    
printResult(1, n1)
printResult(2, n2)
