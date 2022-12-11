
from utils import Input, printResult

# https://adventofcode.com/2022/day/10

input = Input(2022, 10).lines()

x = 1
cycle = 0
strength = [0]
crt = [[' '] * 40 for _ in range(6)]

def check(n, x):
    if n % 40 == 20:
        strength[0] += n * x
    row, col = (n-1) // 40, (n-1) % 40
    if abs(col - x) < 2:
        crt[row][col] = '#'

for s in input:
    if s == 'noop':
        check(cycle + 1, x)
        cycle += 1
    else:
        check(cycle + 1, x)
        check(cycle + 2, x)
        x += int(s[4:])
        cycle += 2

printResult(1, strength[0])
print('\n' + '\n'.join(map(''.join, crt)))
