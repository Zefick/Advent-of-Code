
from utils import Input, printResult

# https://adventofcode.com/2021/day/3

input = Input(2021, 3).lines()

n = len(input[0])

def most(arr, pos):
    n = sum(map(lambda s: s[pos] == '1', arr))
    return '1' if n >= len(arr) / 2 else '0'

def least(arr, pos):
    n = sum(map(lambda s: s[pos] == '1', arr))
    return '0' if n >= len(arr) / 2 else '1'

gamma = "".join(map(lambda i: most(input, i), range(n)))
epsilon = "".join(map(lambda i: least(input, i), range(n)))

printResult(1, int(gamma, 2) * int(epsilon, 2))

a, b = input, input.copy()

for i in range(n):
    if len(a) > 1:
        x = most(a, i)
        a = list(filter(lambda s: s[i] == x, a))

    if len(b) > 1:
        x = least(b, i)
        b = list(filter(lambda s: s[i] == x, b))

printResult(2, int(a[0], 2) * int(b[0], 2))
