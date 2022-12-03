
from utils import Input, printResult

# https://adventofcode.com/2021/day/24

input = Input(2021, 24).lines()

''' reference implementation '''
def run_native(program, input) :
    mem = [0] * 4
    vars = "wxyz"
    i = 0
    for s in program:
        if not s or s[0] == '#':
            continue
        parts = s.split()
        if parts[0] == 'inp':
            mem[vars.index(parts[1])] = input[i]
            i += 1
        else:
            a = vars.index(parts[1])
            b = mem[vars.index(parts[2])] if parts[2] in vars else int(parts[2])
            if parts[0] == 'add':
                mem[a] += b
            elif parts[0] == 'mul':
                mem[a] *= b
            elif parts[0] == 'div':
                mem[a] //= b
            elif parts[0] == 'mod':
                mem[a] %= b
            elif parts[0] == 'eql':
                mem[a] = int(mem[a] == b)
    return mem[3]

''' compiled version '''
def run(input) :
    z0 =           input[0] + 13
    z1 = z0 * 26 + input[1] + 16
    z2 = z1 * 26 + input[2] + 2
    z3 = z2 * 26 + input[3] + 8
    z4 = z3 * 26 + input[4] + 11
    x = (z4 % 26 - 11) != input[5]
    z5 = (z4 // 26) * (25 * x + 1) + (input[5] + 6) * x
    x = (z5 % 26 + 1) != input[6]
    z6 = z5 * (25 * x + 1) + (input[6] + 12) * x
    x = (z6 % 26 - 16) != input[7]
    z7 = (z6 // 26) * (25 * x + 1) + (input[7] + 2) * x
    x = (z7 % 26 - 9) != input[8]
    z8 = (z7 // 26) * (25 * x + 1) + (input[8] + 2) * x
    z9 = z8 * 26 + input[9] + 15
    x = (z9 % 26 - 8) != input[10]
    z10 = (z9 // 26) * (25 * x + 1) + (input[10] + 1) * x
    x = (z10 % 26 - 8) != input[11]
    z11 = (z10 // 26) * (25 * x + 1) + (input[11] + 10) * x
    x = (z11 % 26 - 10) != input[12]
    z12 = (z11 // 26) * (25 * x + 1) + (input[12] + 14) * x
    x = (z12 % 26 - 9) != input[13]
    z13 = z12 // 26 * (25 * x + 1) + (input[13] + 10) * x
    return z13

''' 
try to guess digits.
Returns False If any important digit cannot be guessed
'''
def check(input) :
    z0 =           input[0] + 13
    z1 = z0 * 26 + input[1] + 16
    z2 = z1 * 26 + input[2] + 2
    z3 = z2 * 26 + input[3] + 8
    z4 = z3 * 26 + input[4] + 11

    w = (z4 % 26 - 11)
    if w > 0 and w < 10:
        input[5] = w
    else:
        return False

    z5 = (z4 // 26)
    z6 = z5 * 26 + input[6] + 12

    w = (z6 % 26 - 16)
    if w > 0 and w < 10:
        input[7] = w
    else:
        return False

    z7 = (z6 // 26)

    w = (z7 % 26 - 9)
    if w > 0 and w < 10:
        input[8] = w
    else:
        return False

    z8 = (z7 // 26)
    z9 = z8 * 26 + input[9] + 15

    w = (z9 % 26 - 8)
    if w > 0 and w < 10:
        input[10] = w
    else:
        return False

    z10 = (z9 // 26)

    w = (z10 % 26 - 8)
    if w > 0 and w < 10:
        input[11] = w
    else:
        return False

    z11 = (z10 // 26)

    w = (z11 % 26 - 10)
    if w > 0 and w < 10:
        input[12] = w
    else:
        return False

    z12 = (z11 // 26)

    w = (z12 % 26 - 9)
    if w > 0 and w < 10:
        input[13] = w
    else:
        return False

    return input

import itertools

def decipher(template) :
    for s in itertools.product(*([template] * 7)):
        mem = list(s)[:5] + [0] * 9
        mem[6] = s[5]
        mem[9] = s[6]
        mem = check(mem)
        if mem is False:
            continue
        z = run(mem)
        if z == 0:
            return "".join(map(str, mem))

printResult(1, decipher(range(9, 0, -1)))
printResult(2, decipher(range(1, 10)))

# 53999995829399
# 11721151118175
