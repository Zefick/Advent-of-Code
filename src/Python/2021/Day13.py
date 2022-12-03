
from utils import Input, printResult

# https://adventofcode.com/2021/day/13

input = Input(2021, 13).lines()

dots = set()
first = True
folds = []

def fold(dots, dir, val):
    dots2 = set()
    for d in dots:
        if dir == 'x' and d[0] > val:
            dots2.add((val + val - d[0], d[1]))
        elif dir == 'y' and d[1] > val:
            dots2.add((d[0], val + val - d[1]))
        else:
            dots2.add(d)
    return dots2

for s in input:
    if len(s) == 0:
         continue
    if len(s) < 10:
        s = s.split(',')
        dots.add((int(s[0]), int(s[1])))
    else:
        dots = fold(dots, s[11], int(s[13:]))
        if first:
            first = False
            printResult(1, len(dots))

w = max(d[0] for d in dots) + 1
h = max(d[1] for d in dots) + 1

screen = list([' '] * w for _ in range(h))
for d in dots:
    screen[d[1]][d[0]] = "#"

printResult(2, "\n" + "\n".join("".join(s) for s in screen))
