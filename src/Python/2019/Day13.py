
import math
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/13

def printScreen(screen):
    minx = min(p[0] for p in screen)
    maxx = max(p[0] for p in screen)
    miny = min(p[1] for p in screen)
    maxy = max(p[1] for p in screen)
    palette = {0: " . ", 1: "@@@", 2: "[#]", 3: "===", 4: " O "}
    image = ""
    for y in range(miny, maxy+1):
        image += "\n" + "".join(
            palette[screen.get((x, y), 0)]
            for x in range(minx, maxx+1))
    print(image)

input = list(map(int, Input(2019, 13).lines()[0].split(",")))

screen = {}
arcade = list(Intcode(input).run())
for i in range(len(arcade) // 3):
    x, y, id = arcade[i*3 : i*3+3]
    screen[(x, y)] = id
    
blocks = sum(cell == 2 for cell in screen.values())
printResult(1, blocks)

#printScreen(screen)

def runArcade(controls):
    input[0] = 2
    arcade = Intcode(input, controls).run()
    score = " ? "
    while True:
        x, y, id = [next(arcade, None) for _ in range(3)]
        if x is None:
            return score
        if x == -1:
            score = id

ball = next(cell[0] for cell in screen.items() if cell[1] == 4)
paddle = next(cell[0] for cell in screen.items() if cell[1] == 3)
controls = []
d = [1, 1]
while blocks > 0:
    if screen[(ball[0] + d[0], ball[1])] == 1:
        d[0] =- d[0]

    if screen[(ball[0], ball[1] + d[1])] == 1:
        d[1] =- d[1]

    if screen[(ball[0] + d[0], ball[1])] == 2:
        screen[(ball[0] + d[0], ball[1])] = 0
        blocks -= 1
        d[0] = -d[0]
    if screen[(ball[0], ball[1] + d[1])] == 2:
        screen[(ball[0], ball[1] + d[1])] = 0
        blocks -= 1
        d[1] = -d[1]
    for _ in range(2):
        if screen[(ball[0] + d[0], ball[1] + d[1])] == 2:
            screen[(ball[0] + d[0], ball[1] + d[1])] = 0
            blocks -= 1
            d = [-d[0], -d[1]]

    if screen[(ball[0] + d[0], ball[1])] == 1:
        d[0] =- d[0]

    if screen[(ball[0], ball[1] + d[1])] == 1 or ball[1] == 20:
        d[1] =- d[1]

    move = 1 if ball[0] > paddle[0] else (-1 if ball[0] < paddle[0] else 0)
    controls.append(move)

    screen[paddle] = 0
    paddle = (paddle[0] + move, paddle[1])
    screen[paddle] = 3

    screen[ball] = 0
    ball = (ball[0] + d[0], ball[1] + d[1])
    screen[ball] = 4

    #printScreen(screen)

printResult(2, runArcade(controls))

