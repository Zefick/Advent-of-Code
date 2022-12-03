
from utils import Input, printResult

# https://adventofcode.com/2021/day/7

input = list(map(int, Input(2021, 7).lines()[0].split(",")))

# input = [16,1,2,0,4,2,7,1,2,14]

m1, m2 = 10 ** 10, 10 ** 10

for p in range(min(input), max(input)):
    s1, s2 = 0, 0
    for x in input:
        n = abs(p-x)
        s1 += n
        s2 += (n * (n+1)) // 2
    m1 = min(m1, s1)
    m2 = min(m2, s2)

printResult(1, m1)
printResult(2, m2)
