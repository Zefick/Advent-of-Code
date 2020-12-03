
import math
from utils import Input, printResult

# https://adventofcode.com/2019/day/16

def sparce_indices(offset, j, n):
    while True:
        for i in range(offset, offset + j):
            if i >= n:
                return
            yield i
        offset += j * 4

def fft(input):
    n = len(input)
    for i in range(100):
        nextInput = []
        for j in range(n):
            s = sum(map(input.__getitem__, sparce_indices(j, (j+1), n))) \
                - sum(map(input.__getitem__, sparce_indices(j + (j+1) * 2, (j+1), n)))
            nextInput.append(abs(s) % 10)
        input = nextInput
    return input

import time
t = time.time()
input = list(map(int, Input(2019, 16).lines()[0]))
printResult(1, "".join(list(map(str, fft(input)))[:8]))
print("%.2f" % (time.time() - t))

t = time.time()
        
def fft2(input):
    input = input[::-1]
    for i in range(100):
        nextInput, s = [], 0
        for i in input:
            s = (s + i) % 10
            nextInput.append(s)
        input = nextInput
    return input[::-1]

offset = int("".join(map(str, input[:7])))
printResult(2, "".join(map(str, fft2(list(input * 10000)[offset:])[:8])))

print("%.2f" % (time.time() - t))

