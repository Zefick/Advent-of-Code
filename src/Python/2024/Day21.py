
from utils import Input, printResult
from functools import cache

# https://adventofcode.com/2024/day/21

input = Input(2024, 21).lines()[:5]

buttons1 = {
    "7": ((0, 0), ">v"), "8": ((0, 1), "<>v"), "9": ((0, 2), "<v"),
    "4": ((1, 0), ">^v"), "5": ((1, 1), "<>^v"), "6": ((1, 2), "<^v"),
    "1": ((2, 0), "^>"), "2": ((2, 1), "<>^v"), "3": ((2, 2), "<^v"),
    "0": ((3, 1), ">^"), 'A': ((3, 2), "<^")
}

buttons2 = {
    'A': {"A": [""], "^": ["<"], ">": ["v"], "v": ["<v", "v<"], "<": ["v<<"]},
    '^': {"^": [""], "A": [">"], "<": ["v<"], ">": ["v>", ">v"]},
    'v': {"v": [""], "A": ["^>", ">^"], "<": ["<"], ">": [">"]},
    '<': {"<": [""], "A": [">>^"], "^": [">^"], "v": [">"]},
    '>': {">": [""], "A": ["^"], "^": ["^<", "<^"], "v": ["<"]},
}

keyboard = ["789", "456", "123", " 0A"]

dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

def num_path(src, dst):
    if src == dst:
        return [""]
    y1, x1 = buttons1[src][0]
    y2, x2 = buttons1[dst][0]
    dist = abs(x2-x1) + abs(y2-y1)
    res = []
    for d in buttons1[src][1]:
        dy, dx = dirs[d]
        if abs(x1+dx-x2) + abs(y1+dy-y2) < dist:
            for p in num_path(keyboard[y1+dy][x1+dx], dst):
                res.append(d + p)
    return res

@cache
def find_path(code, keypad):
    if len(code) == 1:
        return [""]
    res = []
    path = num_path(code[0], code[1]) if keypad == 1 else buttons2[code[0]][code[1]]
    for p1 in path:
        for p2 in find_path(code[1:], keypad):
            res.append(p1 + "A" + p2)
    return res
    
@cache
def find_best(p, n):
    p = "A" + p
    if n == 1:
        return len(find_path(p, 2)[0])
    res = 0
    for i in range(1, len(p)):
        res += min(find_best(p2, n-1) for p2 in find_path(p[i-1] + p[i], 2))
    return res

part1, part2 = 0, 0
for code in input:
    part1 += min(find_best(p, 2) for p in find_path("A" + code, 1)) * int(code[:-1])
    part2 += min(find_best(p, 25) for p in find_path("A" + code, 1)) * int(code[:-1])

printResult(1, part1)
printResult(2, part2)
