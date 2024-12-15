
from utils import Input, printResult
from itertools import product

# https://adventofcode.com/2024/day/15

input = Input(2024, 15).lines()

field, moves = [], []
for line in input:
    if line:
        if line[0] == '#':
            if '@' in line:
                start = (len(field), line.index('@'))
            field.append(list(line))
        else:
            moves.append(line)
field[start[0]][start[1]] = '.'
moves = "".join(moves)

field2 = []
d = {'#': '##', '.': '..', 'O': '[]', '@': '@.'}
for line in field:
    field2.append(sum((list(d[c]) for c in line), []))

dirs = {'^': (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0,-1)}
y, x = start
for m in moves:
    dy, dx = dirs[m]
    y2, x2 = y + dy, x + dx
    if field[y2][x2] == '.':
        x, y = x2, y2
    elif field[y2][x2] == 'O':
        for i in range(2, 100):
            if field[y+dy*i][x+dx*i] == 'O':
                continue
            if field[y+dy*i][x+dx*i] == '#':
                break
            elif field[y+dy*i][x+dx*i] == '.':
                field[y+dy*i][x+dx*i] = 'O'
                field[y+dy][x+dx] = '.'
                x, y = x2, y2
                break

part1 = 0
h, w = len(field), len(field[0])
for y, x in product(range(h), range(w)):
    if field[y][x] == 'O':
        part1 += y*100 + x

printResult(1, part1)

def check_move(x, y , dx, dy):
    if dy == 0:
        for i in range(2, 100):
            if field[y][x+dx*i] in '[]':
                continue
            if field[y][x+dx*i] == '#':
                return False
            elif field[y][x+dx*i] == '.':
                return True
    else:
        dx = 1 if field[y+dy][x] == '[' else -1
        if field[y+dy*2][x] == '.' and field[y+dy*2][x+dx] == '.':
            return True
        elif field[y+dy*2][x] == '#' or field[y+dy*2][x+dx] == '#':
            return False
        else:
            return (field[y+dy*2][x] == '.' or check_move(x, y+dy, 0, dy)) and \
                   (field[y+dy*2][x+dx] == '.' or check_move(x+dx, y+dy, 0, dy))
            
def make_move(x, y, dx, dy):
    if dy == 0:
        for i in range(2, 100):
            if field[y][x+dx*i] == '.':
                for j in range(i,0,-1):
                    field[y][x+dx*j] = field[y][x+dx*(j-1)]
                break
    else:
        dx = 1 if field[y+dy][x] == '[' else -1
        if field[y+dy*2][x] in '[]':
            make_move(x, y+dy, 0, dy)
        if field[y+dy*2][x+dx] in '[]':
            make_move(x+dx, y+dy, 0, dy)
        field[y+dy*2][x] = field[y+dy][x]
        field[y+dy*2][x+dx] = field[y+dy][x+dx]
        field[y+dy][x] = '.'
        field[y+dy][x+dx] = '.'

field = field2
y, x = start[0], start[1]*2
i = 0
for m in moves:
    dy, dx = dirs[m]
    y2, x2 = y + dy, x + dx
    if field[y2][x2] == '.':
        x, y = x2, y2
    elif field[y2][x2] in '[]':
        if check_move(x, y, dx, dy):
            make_move(x, y, dx, dy)
            x, y = x2, y2
    # field[y][x] = m
    # print("\n".join("".join(line) for line in field))
    # print(i)
    # i += 1
    # field[y][x] = '.'

part2 = 0
h, w = len(field), len(field[0])
for y, x in product(range(h), range(w)):
    if field[y][x] == '[':
        part2 += y*100 + x
printResult(2, part2)
