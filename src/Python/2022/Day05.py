
from utils import Input, printResult
import re

# https://adventofcode.com/2022/day/5

input = iter(Input(2022, 5).lines())
crates = [[] for _ in range(9)]

for line in input:
    if not line:
        break
    for i in range(len(line) // 4 + 1):
        c = line[1 + i*4]
        if c.isalpha():
            crates[i].append(c)
            
for i in range(9):
    crates[i] = crates[i][::-1]

crates1 = crates
crates2 = [list(x) for x in crates]

p = re.compile("move (\d+) from (\d+) to (\d+)")
for line in input:
    m = p.match(line)
    n = int(m[1])
    src1 = crates1[int(m[2])-1]
    src2 = crates2[int(m[2])-1]
    dst1 = crates1[int(m[3])-1]
    tmp = []
    for i in range(n):
        dst1.append(src1.pop())
        tmp.append(src2.pop())
    crates2[int(m[3])-1] += tmp[::-1]
        
printResult(1, "".join(x[-1] for x in crates1))
printResult(2, "".join(x[-1] for x in crates2))
