
from utils import Input, printResult

# https://adventofcode.com/2024/day/17

input = Input(2024, 17).lines()
regs = [int(input[i][12:]) for i in range(3)]
program = list(map(int, input[4][9:].split(",")))

def run(regs, program):
    def combo(n):
        return n if n < 4 else regs[n-4]
    output, ptr = [], 0
    while ptr < len(program):
        op, x = program[ptr: ptr+2]
        if op == 3 and regs[0] != 0:
            ptr = x
            continue
        if   op == 0: regs[0] = regs[0] >> combo(x)
        elif op == 1: regs[1] ^= x
        elif op == 2: regs[1] = combo(x) % 8
        elif op == 4: regs[1] ^= regs[2]
        elif op == 5: output.append(combo(x) % 8)
        elif op == 6: regs[1] = regs[0] >> combo(x)
        elif op == 7: regs[2] = regs[0] >> combo(x)
        ptr += 2
    return output

printResult(1, ",".join(map(str, run(regs, program))))

# print(run([int("123456", 8), 0, 0], [5,4,0,3,3,0]))

# since we doesn't know anything about the input program in general,
# there is no reliable way to solve it for any input programmatically
# and trying to solve it for only one input violates copyright rules
