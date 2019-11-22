
from utils import Input, printResult

# https://adventofcode.com/2018/day/21

R4, R5 = 0, 0
visited = set()
R4prev = 0
while True:
    # line 6
    R5 = R4 | 0x10000
    R4 = 1765573
    # line 8
    while True:
        R4 += R5 & 255
        R4 = ((R4 & 0xFFFFFF) * 65899) & 0xFFFFFF
        if R5 < 256:
            break
        R5 //= 256
    # line 29
    if R4 in visited:
        printResult(2, R4prev)
        break
    else:
        if len(visited) == 0:
            printResult(1, R4)
        visited.add(R4)
    R4prev = R4
