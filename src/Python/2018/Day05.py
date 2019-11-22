
from utils import Input, printResult

# https://adventofcode.com/2018/day/5

def react(polymer : str) :
    while True:
        l = len(polymer)
        for c in range(26):
            c2 = chr(ord('a') + c)
            polymer = polymer.replace(c2 + c2.upper(), "")
            polymer = polymer.replace(c2.upper() + c2, "")
        if len(polymer) == l:
            break
    return polymer

polymer = Input(2018, 5).lines()[0]
polymer = react(polymer)
printResult(1, len(polymer))

m = len(polymer)
for c in range(26):
    c2 = chr(ord('a') + c)
    m = min(m, len(react(polymer.replace(c2, "").replace(c2.upper(), ""))))
printResult(2, m)
