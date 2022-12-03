
from utils import Input, printResult

# https://adventofcode.com/2021/day/11

input = Input(2021, 11).lines()

for i in range(len(input)):
    input[i] = list(map(int, input[i]))

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def flash(map, x, y) :
    map[y][x] = '*'
    for dx, dy in deltas:
        x2, y2 = x + dx, y + dy
        if x2 >= 0 and x2 < 10 and y2 >=0 and y2 < 10 and map[y2][x2] != '*':
            map[y2][x2] += 1
            if map[y2][x2] > 9:
                flash(map, x2, y2)

flashes = 0
for i in range(10000):
    if i == 100:
        printResult(1, flashes)
    for y in range(10):
        for x in range(10):
            if input[y][x] != '*':
                input[y][x] += 1
                if input[y][x] > 9:
                    flash(input, x, y)
    if all(s.count('*') == 10 for s in input):
        printResult(2, i+1)
        break
    for y in range(10):
        for x in range(10):
            if input[y][x] == '*':
                flashes += 1
                input[y][x] = 0
