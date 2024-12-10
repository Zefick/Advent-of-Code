
from utils import Input, printResult

# https://adventofcode.com/2024/day/9

input = list(map(int, Input(2024, 9).lines()[0]))

disk = []
id = 0
for i, x in enumerate(input):
    if (x > 0):
        if i % 2 == 0:
            disk += [id] * x
            id += 1
        else:
            disk += [-1] * x

disk1 = list(disk)
i, j = 0, len(disk)-1
while i < j:
    while i < j and disk1[i] != -1:
        i += 1
    while i < j and disk1[j] == -1:
        j -= 1
    if i < j:
        disk1[i], disk1[j] = disk1[j], -1

def checksum(disk):
    return sum(i * x for (i, x) in enumerate(disk) if x != -1)

printResult(1, checksum(disk1))

disk2 = list(disk)
gaps = []
files = []
j, id = 0, 0
for i, ln in enumerate(input):
    if (ln > 0):
        if i % 2 == 0:
            files.append((j, ln, id))
            id += 1
        else:
            gaps.append((j, ln))
    j += ln

for pos, ln, id in files[::-1]:
    g = 0
    while g < len(gaps) and gaps[g][1] < ln:
        g += 1
    if g < len(gaps) and  gaps[g][0] <= pos:
        for i in range(ln):
            disk2[gaps[g][0] + i] = id
            disk2[pos + i] = -1
        if gaps[g][1] > ln:
            # use the rest as a new gap
            gaps.append((gaps[g][0] + ln, gaps[g][1] - ln))
        del gaps[g]
        gaps.sort()

printResult(2, checksum(disk2))
