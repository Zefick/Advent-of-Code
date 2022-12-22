
from utils import Input, printResult
from collections import deque

# https://adventofcode.com/2022/day/13

input = Input(2022, 13).lines()
        
def parse(s):
    if type(s) == str:
        s = deque(s)
    if s[0] == '[':
        s.popleft()
        return parse_array(s)
    else:
        val = 0
        while '0' <= (x := s[0]) <= '9':
            val = val * 10 + int(x)
            s.popleft()
        return val
    
def parse_array(s):
    res = []
    while s[0] != ']':
        res.append(parse(s))
        if s[0] == ',':
            s.popleft()
    s.popleft()
    return res


def cmp(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    else :
        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
            
    for i in range(len(a)):
        if len(b) < i+1:
            return 1
        if (res := cmp(a[i], b[i])) != 0:
            return res

    return len(a) - len(b)


packets = []
n  = (len(input) + 1) // 3
s = 0
for i in range(n):
    a = parse(input[i*3])
    b = parse(input[i*3+1])
    packets.append(a)
    packets.append(b)
    if cmp(a, b) < 0:
        s += i + 1

printResult(1, s)

i = 1 + sum(cmp(p, [[2]]) < 0 for p in packets)
j = 2 + sum(cmp(p, [[6]]) < 0 for p in packets)

printResult(2, i * j)
