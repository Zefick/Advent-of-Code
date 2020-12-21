
from utils import Input, printResult

# https://adventofcode.com/2020/day/11

input = Input(2020, 11).lines()

input = ['.' * (len(input[0]) + 2)] + list(map(lambda x: '.' + x + '.', input)) + ['.' * (len(input[0]) + 2)]
cols, rows = len(input[0]), len(input)

def adj1(M, x, y):
    return [M[y-1][x-1], M[y-1][x], M[y-1][x+1], M[y][x-1],
            M[y][x+1], M[y+1][x-1], M[y+1][x], M[y+1][x+1]]

def adj2(M, x, y):
    res = []
    r, c = len(M), len(M[0])
    pred = '.'.__ne__
    res += next(filter(pred, map(lambda i: M[y-i-1][x-i-1], range(min(x, y)))), [])
    res += next(filter(pred, map(lambda i: M[y-i-1][x+i+1], range(min(y, c-x-1)))), [])
    res += next(filter(pred, map(lambda i: M[y-i-1][x], range(y))), [])
    res += next(filter(pred, map(lambda i: M[i][x], range(y+1, r))), [])
    res += next(filter(pred, map(lambda i: M[y][x-i-1], range(x))), [])
    res += next(filter(pred, map(lambda i: M[y][i], range(x+1, c))), [])
    res += next(filter(pred, map(lambda i: M[y+i+1][x-i-1], range(min(x, r-y-1)))), [])
    res += next(filter(pred, map(lambda i: M[y+i+1][x+i+1], range(min(c-x-1, r-y-1)))), [])
    return res

def process_map(M1, adj, tolerance):
    while True:
        M2 = [['.'] * cols for _ in range(rows)]
        for y in range(1, rows-1):
            for x in range(1, cols-1):
                if M1[y][x] == '.':
                    continue
                acc = adj(M1, x, y).count('#')
                if M1[y][x] == 'L': M2[y][x] = ['L','#'][acc == 0]
                if M1[y][x] == '#': M2[y][x] = ['#','L'][acc >= tolerance]
        if M2 == M1:
            return "".join(map("".join, M2)).count('#')
        M1 = M2

import time
t = time.time()
printResult(2, process_map(input, adj1, 4))
print(time.time() - t)

t = time.time()
printResult(2, process_map(input, adj2, 5))
print(time.time() - t)
