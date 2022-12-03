
from utils import Input, printResult

# https://adventofcode.com/2021/day/9

input = Input(2021, 9).lines()

adj = [[-1, 0], [1, 0], [0, -1], [0, 1]]
risk = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        b = True
        for a in adj:
            y2, x2 = y+a[0], x+a[1]
            if y2 >= 0 and y2 < len(input) and x2 >= 0 and x2 < len(input[0]):
                if input[y2][x2] <= input[y][x]:
                    b = False
        if b:
            risk += int(input[y][x]) + 1

printResult(1, risk)

basins = {}
def visit(map, x, y, basin) :
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack.pop()
        for a in adj:
            y2, x2 = y+a[0], x+a[1]
            if y2 >= 0 and y2 < len(map) and x2 >= 0 and x2 < len(map[0]):
                if map[y2][x2] != '9' and (x2, y2) not in basins:
                    basins[(x2, y2)] = basin
                    stack.append((x2, y2))

n = 1
for y in range(len(input)):
    for x in range(len(input[0])):
        if (x, y) not in basins and input[y][x] != '9':
            visit(input, x, y, n)
            n += 1

m = [list(basins.values()).count(i) for i in range(1, n)]
m = list(sorted(m))[::-1]

printResult(2, m[0] * m[1] * m[2])
