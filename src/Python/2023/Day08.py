
from utils import Input, printResult

# https://adventofcode.com/2023/day/8

input = Input(2023, 8).lines()

instructions = input[0]

map = {}
for line in input[2:]:
    a, b, c = line[:3], line[7:10], line[12:15]
    map[a] = (b, c)

state = 'AAA'
i = 0
steps = 1
while True:
    c = instructions[i]
    state = map[state][0] if c == 'L' else map[state][1]
    if (state == 'ZZZ'):
        break
    i = (i + 1) % len(instructions)
    steps += 1

printResult(1, steps)

state = []
for k in map.keys():
    if k[2] == 'A':
        state.append(k)
start = state.copy()

distances = []
i, steps = 0, 0
while len(distances) < len(start):
    c = instructions[i]
    next_state = []
    for j, node in enumerate(state):
        next_state.append(map[state[j]][0] if c == 'L' else map[state[j]][1])
        if next_state[j][2] == 'Z' and i == len(instructions) - 1:
            distances.append(steps + 1)
    state = next_state
    i = (i + 1) % len(instructions)
    steps += 1
    
import math
from functools import reduce
printResult(2, reduce(math.lcm, distances))
