
from utils import Input, printResult

# https://adventofcode.com/2021/day/2

input = Input(2021, 2).lines()

x, y, z = 0, 0, 0
for s in input:
    a, b = s.split()
    b = int(b)
    if a[0] == 'f':
        x += b
        y += z * b
    elif a[0] == 'u':
        z -= b
    elif a[0] =='d':
        z += b

printResult(1, x * z)
printResult(2, x * y)
