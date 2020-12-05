
from utils import Input, printResult

# https://adventofcode.com/2020/day/5

input = Input(2020, 5).lines()

part1 = 0
seats = set()
for line in input:
    line = line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    n = int(line, 2)
    part1 = max(part1, n)
    seats.add(n)

part2 = next(filter(lambda x: x not in seats, range(min(seats), max(seats))))

printResult(1, part1)
printResult(2, part2)
