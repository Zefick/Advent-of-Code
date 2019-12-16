
import math
from utils import Input, printResult

# https://adventofcode.com/2019/day/14

recipes = {}
for line in Input(2019, 14).lines():
    left, right = line.split(" => ")
    left = [(int(x), y) for x, y in [c.split(" ") for c in left.split(", ")]]
    right = right.split(" ")
    recipes[right[1]] = (int(right[0]), left)

def calcOre(n):
    need = {"FUEL": n}
    ore, stock = 0, {}
    while len(need) > 0:
        elem, n = next(iter(need.items()))
        del need[elem]
        if elem in stock:
            x = min(n, stock[elem])
            n -= x
            stock[elem] -= x
        if n == 0:
            continue
        q, components = recipes[elem]
        times = ((n-1) // q + 1)
        for m, e in components:
            if e == "ORE":
                ore += m * times
            else:
                need[e] = need.get(e, 0) + m * times
        if n % q > 0:
            stock[elem] = stock.get(elem, 0) + (q - n % q)
    return ore

printResult(1, calcOre(1))

a, b = [1, 10**8]
while b > a+1:
    mid = (a + b) // 2
    if calcOre(mid) <= 10**12:
        a = mid
    else:
        b = mid

printResult(2, a)

