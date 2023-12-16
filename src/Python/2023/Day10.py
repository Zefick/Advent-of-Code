
from utils import Input, printResult

# https://adventofcode.com/2023/day/10

input = list(map(list, Input(2023, 10).lines()))

h, w = len(input), len(input[0])

# array for the second part
input2 = [['.'] * w for _ in range(h)]

start = next((y, x) for y in range(h) for x in range(w) if input[y][x] == 'S')
input[start[0]][start[1]] = '7'

dirs = {
    '-': {'>': (0, 1, '>'), '<': (0, -1, '<')},
    '|': {'v': (1, 0, 'v'), '^': (-1, 0, '^')},
    'J': {'>': (-1, 0, '^'), 'v': (0, -1, '<')},
    '7': {'>': (1, 0, 'v'), '^': (0, -1, '<')},
    'L': {'v': (0, 1, '>'), '<': (-1, 0, '^')},
    'F': {'^': (0, 1, '>'), '<': (1, 0, 'v')},
}

cur = start
steps = 0
prev = start
dir = '>'
while True:
    y, x = cur
    dx, dy, dir = dirs[input[y][x]][dir]
    y2, x2 = y + dx, x + dy
    input2[y][x] = "#" if input[y][x] in "|7F" else "*"
    prev, cur = (y, x), (y2, x2)
    steps += 1
    if cur == start:
        break

printResult(1, steps // 2)

# A point is inside a cycle if it has an odd number of pipe crossings on both sides
# since total number of crossings in one line is always even,
# we just have to check the number of crossings on the left side
# an imaginary horizontal line crosses the loop if it goes through one of the symbols '|', '7' or 'F' 
# which already marked as '#' in the input2 matrix
n = 0
for y in range(h):
    for x in range(w):
        n += input2[y][x] == '.' and input2[y][:x].count('#') % 2

printResult(2, n)
