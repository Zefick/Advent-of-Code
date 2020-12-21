
from utils import Input, printResult

# https://adventofcode.com/2020/day/13

input = Input(2020, 13).lines()
timestamp = int(input[0])
shedules = input[1].split(',')

buses = map(int, filter('x'.__ne__, shedules))
earliest = min(((b, b - timestamp % b) for b in buses), key = lambda x: x[1])
printResult(1, earliest[0] * earliest[1])

def find_time2(t1, t2, i, mul):
    return next(x for x in range(t1, t2*mul, mul) if (x + i) % t2 == 0)

mul, time = 1, 0
for i, b in enumerate(shedules):
    if b != 'x':
        b = int(b)
        time = find_time2(time, b, i, mul)
        mul *= b
printResult(2, time)
