
# https://adventofcode.com/2018/day/19

def makeOpcode(opcode):
    def doOperation(inst, args, opcode): 
        res = list(args)
        res[inst[3]] = opcode(inst, args)
        return res
    return lambda inst, args: doOperation(inst, args, opcode)

opcodes = {
    "addr": makeOpcode(lambda inst, args: args[inst[1]] + args[inst[2]]),
    "addi": makeOpcode(lambda inst, args: args[inst[1]] + inst[2]),
    "mulr": makeOpcode(lambda inst, args: args[inst[1]] * args[inst[2]]),
    "muli": makeOpcode(lambda inst, args: args[inst[1]] * inst[2]),
    "banr": makeOpcode(lambda inst, args: args[inst[1]] & args[inst[2]]),
    "bani": makeOpcode(lambda inst, args: args[inst[1]] & inst[2]),
    "borr": makeOpcode(lambda inst, args: args[inst[1]] | args[inst[2]]),
    "bori": makeOpcode(lambda inst, args: args[inst[1]] | inst[2]),
    "setr": makeOpcode(lambda inst, args: args[inst[1]]),
    "seti": makeOpcode(lambda inst, args: inst[1]),
    "gtir": makeOpcode(lambda inst, args: 1 if inst[1] > args[inst[2]] else 0),
    "gtri": makeOpcode(lambda inst, args: 1 if args[inst[1]] > inst[2] else 0),
    "gtrr": makeOpcode(lambda inst, args: 1 if args[inst[1]] > args[inst[2]] else 0),
    "eqir": makeOpcode(lambda inst, args: 1 if inst[1] == args[inst[2]] else 0),
    "eqri": makeOpcode(lambda inst, args: 1 if args[inst[1]] == inst[2] else 0),
    "eqrr": makeOpcode(lambda inst, args: 1 if args[inst[1]] == args[inst[2]] else 0),
}

from utils import Input
import re

p = re.compile("(\\w+) (\\d+) (\\d+) (\\d+)")
program = []
ip = 3
for line in Input(2018, 19).lines()[1:]:
    m = p.match(line)
    program.append([m[1], int(m[2]), int(m[3]), int(m[4])])

from utils import printResult

for v in [0, 1]:
    regs = [v, 0, 0, 0, 0, 0]
    for t in range(1000):
        if regs[ip] < 0 or regs[ip] >= len(program):
            break
        inst = program[regs[ip]]
        regs = opcodes[inst[0]](inst, regs)
        regs[ip] += 1
    printResult(v+1, regs[5] + regs[5] // 2 + 3)
