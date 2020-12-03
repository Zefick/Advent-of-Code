
import math
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/17

input = list(map(int, Input(2019, 17).lines()[0].split(",")))

intcode = list(Intcode(input).run())
image = "".join(chr(c) for c in intcode).strip().split("\n")
#print("\n".join(image))
s = 0
for y in range(1, len(image)-1):
    for x in range(1, len(image[y])-1):
        if image[y][x-1:x+2] + image[y-1][x] + image[y+1][x] == '#####':
            s += x * y

printResult(1, s)

# PART 2

# aading borders
image = ['.' * len(image[0])] + image + ['.' * len(image[0])]
for y in range(len(image)):
    image[y] = '.' + image[y] + '.'
    for x in range(len(image[y])):
        if   image[y][x] == '^': p = [x, y, 0, -1]
        elif image[y][x] == 'v': p = [x, y, 0, 1]
        elif image[y][x] == '<': p = [x, y, -1, 0]
        elif image[y][x] == '>': p = [x, y, 1, 0]

# build path
path = ""
steps = 0
while True:
    if image[p[1] + p[3]][p[0] + p[2]] == '.':
        path += str(steps) + ","
        steps = 0
        for (dir, dx, dy) in [["L", p[3], -p[2]], ["R", -p[3], p[2]]]:
            if image[p[1] + dy][p[0] + dx] == '#':
                p = p[:2] + [dx, dy]
                path += dir + ","
                break
        else:
            break
    p = [p[0] + p[2], p[1] + p[3]] + p[2:]
    steps += 1

path = path[2:]

def findSegments(path, result, segments, n):
    while True:
        if len(path) == 0:
            return result
        for i in range(n):
            if path.startswith(segments[i]):
                path = path[len(segments[i]):]
                result += chr(ord('A')+i) + ','
                break
        else:
            break
    if n == 3:
        return None
    for i in range(1, 22):
        if path[i-1] != ',': continue
        segments[n] = path[:i]
        found = findSegments(path, result, segments, n+1)
        if found:
            return found

# search for optimal segments
segments = [""] * 3
routine = findSegments(path, "", segments, 0)

input[0] = 2
commands = list(map(ord, '\n'.join([routine[:-1], segments[0][:-1], segments[1][:-1], segments[2][:-1], 'n\n'])))
output = list(Intcode(input, commands).run())
printResult(2, output[-1])
