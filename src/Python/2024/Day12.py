
from utils import Input, printResult
from itertools import product

# https://adventofcode.com/2024/day/12

input = Input(2024, 12).lines()

# add borders
input = ['.' + line + '.' for line in input]
input = ['.' * len(input[0])] + input + ['.' * len(input[0])]

h, w = len(input), len(input[0])

visited = set()

def scan_region(y, x):
    q = [(y, x)]
    p, s = 0, 0
    planks_h = set()
    planks_v = set()
    while q:
        y, x = q.pop()
        if (y, x) in visited:
            continue
        c = input[y][x]
        visited.add((y, x))
        s += 1
        
        for d in [1, -1]:
            if input[y][x+d] != c:
                planks_v.add((y, x, d))
            else:
                q.append((y, x+d))

            if input[y+d][x] != c:
                planks_h.add((y, x, d))
            else:
                q.append((y+d, x))
                
    sides = 0
    for y, x, side in planks_h:
        if (y, x+1, side) not in planks_h:
            sides += 1
        
    for y, x, side in planks_v:
        if (y+1, x, side) not in planks_v:
            sides += 1

    return (s, len(planks_h) + len(planks_v), sides)
    
part1, part2 = 0, 0
for y, x in product(range(1, h-1), range(1, w-1)):
    a, b, c = scan_region(y, x)
    part1 += a * b
    part2 += a * c

printResult(1, part1)
printResult(2, part2)
