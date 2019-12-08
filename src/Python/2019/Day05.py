
from utils import Input, printResult

# https://adventofcode.com/2019/day/5

input = list(map(int, Input(2019, 5).lines()[0].split(",")))

def run(input, x):
    ptr = 0
    output = []
    shifts = {1:4, 2:4, 3:2, 4:2, 7:4, 8:4}
    while input[ptr] != 99:
        code = input[ptr]
        op = code % 100
        a, b, c = input[ptr+1:ptr+4]
        if op in [1, 2, 4, 5, 6, 7, 8] and code // 100 % 10 == 0:
            a = input[a]
        if op in [1, 2, 5, 6, 7, 8] and code // 1000 % 10 == 0:
            b = input[b]
        if op == 1:
            input[c] = a + b
        elif op == 2:
            input[c] = a * b
        elif op == 3:
            input[a] = x
        elif op == 4:
            output.append(a)
        elif op == 5:
            ptr = b if a != 0 else ptr + 3
        elif op == 6:
            ptr = b if a == 0 else ptr + 3
        elif op == 7:
            input[c] = int(a < b)
        elif op == 8:
            input[c] = int(a == b)
        ptr += shifts.get(op, 0)

    return output

printResult(1, run(list(input), 1)[-1])
printResult(2, run(list(input), 5)[-1])
