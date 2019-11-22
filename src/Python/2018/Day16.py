
from utils import Input, printResult
import re

# https://adventofcode.com/2018/day/16

def makeOpcode(opcode):
    def doOperation(inst, args, opcode): 
        res = list(args)
        res[inst[3]] = opcode(inst, args)
        return res
    return lambda inst, args: doOperation(inst, args, opcode)

opcodes = [
    makeOpcode(lambda inst, args: args[inst[1]] + args[inst[2]]),
    makeOpcode(lambda inst, args: args[inst[1]] + inst[2]),
    makeOpcode(lambda inst, args: args[inst[1]] * args[inst[2]]),
    makeOpcode(lambda inst, args: args[inst[1]] * inst[2]),
    makeOpcode(lambda inst, args: args[inst[1]] & args[inst[2]]),
    makeOpcode(lambda inst, args: args[inst[1]] & inst[2]),
    makeOpcode(lambda inst, args: args[inst[1]] | args[inst[2]]),
    makeOpcode(lambda inst, args: args[inst[1]] | inst[2]),
    makeOpcode(lambda inst, args: args[inst[1]]),
    makeOpcode(lambda inst, args: inst[1]),
    makeOpcode(lambda inst, args: 1 if inst[1] > args[inst[2]] else 0),
    makeOpcode(lambda inst, args: 1 if args[inst[1]] > inst[2] else 0),
    makeOpcode(lambda inst, args: 1 if args[inst[1]] > args[inst[2]] else 0),
    makeOpcode(lambda inst, args: 1 if inst[1] == args[inst[2]] else 0),
    makeOpcode(lambda inst, args: 1 if args[inst[1]] == inst[2] else 0),
    makeOpcode(lambda inst, args: 1 if args[inst[1]] == args[inst[2]] else 0),
]

lines = Input(2018, 16).lines()
part1 = 0
posibilities = [list(opcodes) for _ in opcodes]
n = 0
p = re.compile(".{9}(\\d+), (\\d+), (\\d+), (\\d+)")
while lines[n].startswith("Before"):
    m = p.match(lines[n])
    args = list(map(int, [m[1], m[2], m[3], m[4]]))
    inst = list(map(int, lines[n+1].split(" ")))
    m = p.match(lines[n+2])
    res = list(map(int, [m[1], m[2], m[3], m[4]]))
    possibleOpcodes = list(filter(lambda op: op(inst, args) == res, opcodes))
    if len(possibleOpcodes) >= 3:
        part1 += 1
    posibilities[inst[0]] = list(filter(\
        lambda x: x in possibleOpcodes, posibilities[inst[0]]))
    n += 4

printResult(1, part1)

for _ in opcodes:
    for [op] in filter(lambda ops: len(ops) == 1, posibilities):
        for pos in posibilities:
            if len(pos) > 1 and op in pos:
                pos.remove(op)

regs = [0, 0, 0, 0]
for line in lines[n+2:]:
    inst = list(map(int, line.split(" ")))
    regs = posibilities[inst[0]][0](inst, regs)

printResult(2, regs[0])
