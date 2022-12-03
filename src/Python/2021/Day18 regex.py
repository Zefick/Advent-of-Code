
from utils import Input, printResult
import re

# https://adventofcode.com/2021/day/18

input = Input(2021, 18).lines()

left_pattern = re.compile(".*\\D(\\d+).*?")
right_pattern = re.compile(".*?(\\d+)")
long_digit_pattern = re.compile(".*?(\\d\\d+)")
near_pair_pattern = re.compile("(\\d+),(\\d+)")
pair_pattern = re.compile(".*(\[(\\d+),(\\d+)\]).*")

def sum_pair(p1, p2):
    return '[' + p1 + ',' + p2 + ']'

def find_nested(pair):
    n = 0
    for i in range(len(pair)):
        c = pair[i]
        if c == '[':
            n += 1
            if n == 5:
                return i
        elif c == ']':
            n -= 1
    return None

def explode_pair(pair, i):
    m2 = near_pair_pattern.match(pair, pos = i+1)
    a, b = int(m2[1]), int(m2[2])
    res = ""
    m = left_pattern.match(pair, endpos = i)
    if m:
        res = pair[:m.start(1)] + str(int(m.group(1)) + a) + pair[m.end(1):i]
    else :
        res = pair[:i]
    res += '0'
    m = right_pattern.match(pair, pos = m2.end(2)+1)
    if m:
        res += pair[m2.end(2)+1:m.start(1)] + str(int(m.group(1)) + b) + pair[m.end(1):]
    else:
        res += pair[m2.end(2)+1:]
    return res

def reduce_pair(pair: str):
    while True:
        i = find_nested(pair)
        if i:
            pair2 = explode_pair(pair, i)
            pair = pair2
            continue
        else:
            m = long_digit_pattern.match(pair)
            if m:
                x = int(m[1])
                pair = pair[:m.start(1)] + '[' + str(x // 2) + ',' + str((x // 2) + x % 2) + ']' + pair[m.start(1)+2:]
            else:
                break
    return pair

def magnitude(pair):
    while True:
        m = pair_pattern.match(pair)
        if m:
            pair = pair[:m.start(1)] + str(int(m[2])*3 + int(m[3])*2) + pair[m.end(1):]
        else:
            return int(pair)

pair = input[0]
for pair2 in input[1:]:
    pair = reduce_pair(sum_pair(pair, pair2))

printResult(1, magnitude(pair))

import time
t = time.time()

m = 0
for a in input:
    for b in input:
        if a != b:
            mag = magnitude(reduce_pair(sum_pair(a, b)))
            m = max(m, mag)

printResult(2, m)

print(time.time() - t)
