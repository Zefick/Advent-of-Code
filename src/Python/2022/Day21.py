
from utils import Input, printResult

# https://adventofcode.com/2022/day/21

input = Input(2022, 21).lines()

d = {}
for s in input:
    op = s[6:]
    d[s[:4]] = op if len(op) > 5 else int(op)
        
ops = {'+': int.__add__, '-': int.__sub__,
       '*': int.__mul__, '/': int.__floordiv__}

def calc(mon):
    if type(d[mon]) == int:
        return d[mon]
    else:
        mon1, op, mon2 = d[mon].split()
        return ops[op](calc(mon1), calc(mon2))
        
printResult(1, calc("root"))

mon1, _, mon2 = d["root"].split()
l, r = 0, int(1e20)
while l < r:
    m = (l + r) // 2
    d["humn"] = m
    x = calc(mon1)
    y = calc(mon2)
    if x <= y:
        r = m
    else:
        l = m + 1

printResult(2, l)
