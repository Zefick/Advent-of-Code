
from utils import Input, printResult

# https://adventofcode.com/2022/day/14

input = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]

input = Input(2022, 14).lines()

rocks = set()

for s in input:
    lines = s.split(' -> ')
    x, y = map(int, lines[0].split(','))
    for line in lines[1:]:
        x2, y2 = map(int, line.split(','))
        if x == x2:
            for i in range(min(y, y2), max(y, y2)+1):
                rocks.add((x, i))
        else:
            for i in range(min(x, x2), max(x, x2)+1):
                rocks.add((i, y))
        x, y = x2, y2

bottom = max(y for _, y in rocks)

def fall():
    x, y = 500, 0
    while True:
        if y == bottom + 1:
            return (x, y)
        if (x, y+1) not in rocks:
            x, y = x, y+1
        elif (x-1, y+1) not in rocks:
            x, y = x-1, y+1
        elif (x+1, y+1) not in rocks:
            x, y = x+1, y+1
        else:
            return (x, y)
        
n = 0
while True:
    x, y = fall()
    if y >= bottom:
        break
    rocks.add((x, y))
    n += 1

printResult(1, n)
        
while True:
    x, y = fall()
    if y == 0:
        break
    rocks.add((x, y))
    n += 1

printResult(2, n + 1)
