
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/25

key1 = 8421034
key2 = 15993936

# key1 = 5764801
# key2 = 17807724

cache = {}
n = 1
for i in range(1, 100000000):
    n = n * 7 % 20201227
    if n in cache: break
    if n == key1:
        print(1, i)
    if n == key2:
        print(2, i)
    cache[n] = i

p1 = cache[key1]
p2 = cache[key2]

n = 1
for _ in range(p1):
    n = n * key2 % 20201227

printResult(1, n)
