
from utils import Input, printResult

# https://adventofcode.com/2023/day/14

input = list(map(list, Input(2023, 14).lines()))

def tilt(input):
    h, w = len(input), len(input[0])
    for i in range(w):
        stop = 0
        for j in range(h):
            if input[j][i] == 'O':
                input[j][i] = '.'
                input[stop][i] = 'O'
                stop += 1
            if input[j][i] == '#':
                stop = j + 1
                
def score(input):
    h, w = len(input), len(input[0])
    return sum(h-i for i in range(h) for j in range(w) if input[i][j] == 'O')

tilt(input)
printResult(1, score(input))

def rotate(input):
    h, w = len(input), len(input[0])
    return [[input[w-i-1][j] for i in range(h)] for j in range(w)]

def hash(input):
    h, w = len(input), len(input[0])
    res = 0
    for i in range(h):
        for j in range(w):
            if input[i][j] == 'O':
                res = res * 31 + (i * 100 + j)
    return res % 1000000007

import time
t = time.time()

d = {}
N = 1000000000
rem = 0
for i in range(1000):
    for _ in range(4):
        tilt(input)
        input = rotate(input)
    h = hash(input)
    if h in d:
        cycle = i - d[h]
        rem = N - (i + cycle * ((N - i) // cycle))
        break
    d[h] = i

for _ in range(rem-1):
    for _ in range(4):
        tilt(input)
        input = rotate(input)

printResult(2, score(input))

print(time.time() - t)