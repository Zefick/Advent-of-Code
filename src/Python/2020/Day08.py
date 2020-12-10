
from utils import Input, printResult

# https://adventofcode.com/2020/day/8

input = Input(2020, 8).lines()

def runBootcode(input):
    sp, acc = 0, 0
    history = set()
    while True:
        if sp in history or sp == len(input):
            break
        history.add(sp)
        code = input[sp].split()
        if code[0] == "acc":
            acc += int(code[1])
        elif code[0] == "jmp":
            sp += int(code[1]) - 1
        sp += 1
    return (sp, acc)

printResult(1, runBootcode(input)[1])

for k in range(len(input)):
    orig = input[k]
    if input[k].startswith("nop"):
        input[k] = "jmp" + input[k][3:]
    else:
        input[k] = "nop" + input[k][3:]

    sp, acc = runBootcode(input)
    if sp == len(input):
        printResult(2, acc)
        break

    input[k] = orig
