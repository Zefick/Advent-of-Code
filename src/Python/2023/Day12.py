
from utils import Input, printResult
from functools import cache

# https://adventofcode.com/2023/day/12

input = Input(2023, 12).lines()

@cache
def check(row, hint):
    if not row:
        return hint == 0
    if hint == 0:
        return row.count('#') == 0
    if row[0] == '.':
        if hint % 100 != 0:
            return 0
        return check(row[1:], hint // 100) + check(row[1:], hint)
    if row[0] == '#':
        if hint % 100 == 0:
            return 0
        return check(row[1:], hint-1)
    if row[0] == '?':
        return check('.' + row[1:], hint) + check('#' + row[1:], hint)

from time import time
t = time()

for part in [1, 2]:
    res = 0
    for k, line in enumerate(input):
        row, hints = line.split()
        hints = list(map(int, hints.split(',')))
        if part == 2:
            row = '?'.join([row] * 5)
            hints *= 5
        hint = 0
        for h in hints[::-1]:
            hint = (hint + h) * 100
        res += check('.' + row, hint)
    printResult(part, res)

print(time() - t)
