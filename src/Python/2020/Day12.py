
from utils import Input, printResult

# https://adventofcode.com/2020/day/12

input = Input(2020, 12).lines()

def navigate(direction, mode):
    pos = [0, 0]
    for line in input:
        if line == 'L90' or line == 'R270':
            direction = [-direction[1], direction[0]]
        elif line == 'R90' or line == 'L270':
            direction = [direction[1], -direction[0]]
        elif line == 'L180' or line == 'R180':
            direction = [-direction[0], -direction[1]]
        else:
            c, n = line[0], int(line[1:])
            if c in 'NSEW':
                (pos if mode else direction)[c in 'SN'] += n if (c in 'NE') else -n
            elif c == 'F':
                pos = [pos[0] + direction[0] * n, pos[1] + direction[1] * n]
    return sum(map(abs, pos))

printResult(1, navigate([1, 0], True))
printResult(2, navigate([10, 1], False))
