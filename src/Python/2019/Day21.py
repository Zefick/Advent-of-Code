
import math
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/21

input = Input(2019, 21).lines()[0]

def run(s):
    code = Intcode(input)
    out = code.run()
    for c in s.upper():
        code.put_input(ord(c))
    output = ""
    while True:
        c = next(out, None)
        if c is None:
            break
        if c > 255:
            return c
        else:
            output += chr(c)
    return output

program = "\n".join([
    "NOT C J",
    "AND D J",
    "NOT A T",
    "OR T J",
    "WALK\n"
])

printResult(1, run(program))

program = "\n".join([
    "OR A J",
    "AND B J",
    "AND C J",
    "NOT J J",
    "AND D J",
    "OR E T",
    "OR H T",
    "AND T J",
    "RUN\n"]
)

printResult(2, run(program))
