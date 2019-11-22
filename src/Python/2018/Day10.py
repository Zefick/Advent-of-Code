
from utils import Input, printResult

# https://adventofcode.com/2018/day/10

stars = Input(2018, 10).match("position=<\\s*(.+),\\s*(.+)> velocity=<\\s*(.+),\\s*(.+)>")
stars = [[int(m[1]), int(m[2]), int(m[3]), int(m[4])] for m in stars]

for n in range(1, 20000):
    x1, x2, y1, y2 = 1000000, -1000000, 1000000, -1000000
    for star in stars:
        star[0] += star[2]
        star[1] += star[3]
        x1 = min(star[0], x1)
        x2 = max(star[0], x2)
        y1 = min(star[1], y1)
        y2 = max(star[1], y2)
    if y2 - y1 < 15:
        printResult(1, "")
        for y in range(y1-2, y2+3):
            s = ""
            for x in range(x1-2, x2+3):
                b = any(star[0] == x and star[1] == y for star in stars)
                s += "#" if b else " "
            print(s)
        printResult(2, n)