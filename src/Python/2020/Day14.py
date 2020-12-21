
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/14

input = Input(2020, 14).lines()
p = re.compile("mem\\[(\\d+)\\] = (\\d+)")

def get_masked_addrs(addr, mask):
    floats = mask.count('X')
    for i in range(2 ** floats):
        addr2 = addr
        n = floats - 1
        for j in range(len(mask)):
            if mask[35-j] == 'X':
                if i & (2 ** n):
                    addr2 |= 2 ** j
                n -= 1
        yield addr2

mem1 = {}
mem2 = {}
for line in input:
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        m = p.match(line)
        addr, val = int(m[1]), int(m[2])
    
        mask1 = int(mask.replace('X', '0'), 2)
        mask2 = int(mask.replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
        mask3 = int(mask.replace("1", "0").replace('X', '1'), 2)
        mem1[addr] = (val | mask1) & ~mask2

        addr = (addr | mask1) & ~mask3
        for x in get_masked_addrs(addr, mask):
            mem2[x] = val

printResult(1, sum(mem1.values()))
printResult(2, sum(mem2.values()))
