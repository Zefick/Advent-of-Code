
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2023/day/15

input = Input(2023, 15).lines()[0].split(',')

def hash(s: str) -> int:
    res = 0
    for c in s:
        c = ord(c)
        res = ((res + c) * 17) % 256
    return res

printResult(1, sum(hash(s) for s in input))

d = defaultdict(list)

for line in input:
    if line[-1] == '-':
        id = line[:-1]
        lenses = d[hash(id)]
        for j in range(len(lenses)):
            len_id, val = lenses[j]
            if len_id == id:
                lenses.remove(lenses[j])
                break
    else:
        id, value = line.split('=')
        lenses = d[hash(id)]
        for j in range(len(lenses)):
            len_id, val = lenses[j]
            if len_id == id:
                lenses[j] = [id, value]
                break
        else:
            lenses.append([id, value])

res2 = 0
for box, lenses in d.items():
    for i, [_, value] in enumerate(lenses):
        res2 += (box + 1) * (i+1) * int(value)

printResult(2, res2)
