
from utils import Input, printResult
from itertools import product

# https://adventofcode.com/2024/day/25

input = Input(2024, 25).lines()

locks, keys = [], []
for i in range(len(input) // 8 + 1):
    arr = [0] * 5
    for j in range(5):
        for k in range(5):
            arr[k] += input[i*8+j+1][k] == '#'
    if input[i*8][0] == '.':
        locks.append(arr)
    else:
        keys.append(arr)

part1 = 0
for lock, key in product(locks, keys):
    if all(lock[i] + key[i] <= 5 for i in range(5)):
        part1 += 1

printResult(1, part1)
