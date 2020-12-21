
from utils import Input, printResult

# https://adventofcode.com/2020/day/15

input = [1,0,15,2,10,13]

last = 0
spoken = {}

for i in range(0, 30000001):
    n = input[i] if i < len(input) else i - spoken.get(last, i)
    spoken[last] = i
    i += 1
    last = n
    if i == 2020:
        printResult(1, last)

printResult(2, last)

