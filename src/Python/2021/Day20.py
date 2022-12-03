
from utils import Input, printResult

# https://adventofcode.com/2021/day/20

input = Input(2021, 20).lines()

alg = input[0]
canvas = set()
for i in range(len(input)-2):
    s = input[i+2]
    for j in range(len(s)):
        if s[j] == '#':
            canvas.add((i, j))

for n in range(50):
    ymin = min(map(lambda p: p[0], canvas))
    ymax = max(map(lambda p: p[0], canvas))
    xmin = min(map(lambda p: p[1], canvas))
    xmax = max(map(lambda p: p[1], canvas))
    canvas2 = set()
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            index = 0
            index += (n % 2 + ((y-1, x-1) in canvas)) % 2 * 256
            index += (n % 2 + ((y-1, x) in canvas)) % 2 * 128
            index += (n % 2 + ((y-1, x+1) in canvas)) % 2 * 64
            index += (n % 2 + ((y, x-1) in canvas)) % 2 * 32
            index += (n % 2 + ((y, x) in canvas)) % 2 * 16
            index += (n % 2 + ((y, x+1) in canvas)) % 2 * 8
            index += (n % 2 + ((y+1, x-1) in canvas)) % 2 * 4
            index += (n % 2 + ((y+1, x) in canvas)) % 2 * 2
            index += (n % 2 + ((y+1, x+1) in canvas)) % 2 * 1
            if ((alg[index] == '#') + n%2) % 2 == 0:
                canvas2.add((y, x))
    canvas = canvas2
    if n == 1:
        printResult(1, len(canvas))

printResult(2, len(canvas))
