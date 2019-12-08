
from utils import Input, printResult

# https://adventofcode.com/2019/day/2

def run(input, noun, verb):
    input[1:3] = noun, verb
    ptr = 0
    while True:
        code = input[ptr]
        if code == 99:
            break
        a, b, c = input[ptr+1:ptr+4]
        if code == 1:
            input[c] = input[a] + input[b]
        elif code == 2:
            input[c] = input[a] * input[b]
        ptr += 4
    return input[0]

input = list(map(int, Input(2019, 2).lines()[0].split(",")))

printResult(1, run(list(input), 12, 2))

for i in range(100):
    for j in range(100):
        if run(list(input), i, j) == 19690720:
            printResult(2, 100 * i + j)
            break
