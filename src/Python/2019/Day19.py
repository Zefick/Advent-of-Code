
import math
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/19

input = Input(2019, 19).lines()[0]

def scan(x, y):
    return next(Intcode(input, [x, y]).run())

s = sum(scan(x, y) for x in range(0, 50) for y in range(0, 50))
printResult(1, s)

x = 0
for y in range(300, 1000):
    x = next(x for x in range(x, 1000) if scan(x, y) == 1)
    if scan(x + 99, y) == 1:
        break

found = False
while not found:
    y += 1
    while scan(x + 99, y) == 1:
        if scan(x, y + 99) == 1:
            found = True
            break
        else:
            x += 1

printResult(2, x * 10000 + y)
