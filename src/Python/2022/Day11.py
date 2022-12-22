
from utils import Input, printResult

# https://adventofcode.com/2022/day/11

input = Input(2022, 11).lines()

n = len(input) // 7 + 1
items, mods, throws = [], [], []
ops = []

for i in range(n):
    it = list(map(int, input[i*7+1].split(": ")[1].split(", ")))
    items.append(it)
    ops.append(input[i*7+2].split("new = ")[1])
    mods.append(int(input[i*7+3].split("by ")[1]))
    throws.append([int(input[i*7+4].split("monkey ")[1]), \
                   int(input[i*7+5].split("monkey ")[1])])

cnt = [0] * n
for i in range(20):
    for j in range(n):
        for item in items[j]:
            old = item
            item = eval(ops[j]) // 3
            dst =  item % mods[j] != 0
            items[throws[j][dst]].append(item)
        cnt[j] += len(items[j])
        items[j] = []
        
cnt = sorted(cnt, reverse=True)
printResult(1, cnt[0] * cnt[1])

# Part 2

items = [list(map(int, input[i*7+1].split(": ")[1].split(", "))) for i in range(n)]

mod = 1
for x in mods:
    mod *= x
    
cnt = [0] * n
for i in range(10000):
    for j in range(n):
        for item in items[j]:
            old = item
            item = eval(ops[j]) % mod
            dst =  item % mods[j] != 0
            items[throws[j][dst]].append(item)
        cnt[j] += len(items[j])
        items[j] = []
        
cnt = sorted(cnt, reverse=True) 
printResult(2, cnt[0] * cnt[1])
