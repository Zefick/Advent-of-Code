
from utils import Input, printResult

# https://adventofcode.com/2022/day/6

input = Input(2022, 6).lines()[0]

for part, n in [[1, 4], [2, 14]]:
    for i in range(n, len(input)):
        if len(set(list(input[i-n:i]))) == n:
            printResult(part, i)
            break
