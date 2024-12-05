
from utils import Input, printResult
from collections import Counter

# https://adventofcode.com/2024/day/1

input = Input(2024, 1).lines()

list1, list2 = [], []

for line in input:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))
    
list1.sort()
list2.sort()

printResult(1, sum((abs(x - y) for x, y in zip(list1, list2))))

c1 = Counter(list1)
c2 = Counter(list2)

printResult(2, sum(c2[x] * n * x for (x, n) in c1.items()))

# let's use the fact that the arrays are already sorted
# this solution actually slower than the previous one

n = len(list1)
dups = 1
j = 0
s = 0
for i in range(n):
    if i == n-1 or list1[i+1] == list1[i]:
        dups += 1
        continue
    while list2[j] < list1[i] and j < len(list2):
        j += 1
    if j == len(list2):
        break
    while list2[j] == list1[i]:
        s += list1[i] * dups
        j += 1
    
printResult(2, s)
