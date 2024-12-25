
from utils import Input, printResult

# https://adventofcode.com/2024/day/24

input = Input(2024, 24).lines()

regs = {}
ops = {}
for line in input:
    if ":" in line:
        reg, val = line.split(": ")
        regs[reg] = int(val)
    if "->" in line:
        line = line.split()
        ops[line[4]] = (line[0], line[1], line[2])

def calc(reg):
    a, op, b = ops[reg]
    a = calc(a) if a in ops else regs[a]
    b = calc(b) if b in ops else regs[b]
    if op == "AND": return a & b
    elif op == "XOR": return a ^ b
    else: return a | b
    
def calc_z():
    res = {}
    for reg, op in ops.items():
        if reg[0] == 'z':
            res[reg] = calc(reg)
    return int("".join(str(res[k]) for k in sorted(res.keys(), reverse=True)), 2)

printResult(1, calc_z())

# no programatical solution for part 2, only the code for checking the fixed circuits

pairs = [["a", "b"], ["c", "d"], ["e", "f"], ["g", "h"]]
for r1, r2 in pairs:
    ops[r1], ops[r2] = ops[r2], ops[r1]

def check(x, y):
    for k in range(46):
        regs[f"x{k:02}"] = (x >> k) & 1
        regs[f"y{k:02}"] = (y >> k) & 1
    z = calc_z()
    print(f"{x:46b} {x:15}\n{y:46b} {y:15}\n{z:46b} {z:15}  {x+y==z}\n")

from random import getrandbits
for j in range(10):
    x = getrandbits(45)
    y = getrandbits(45)
    check(x, y)

printResult(2, ",".join(sorted(sum(pairs, []))))
