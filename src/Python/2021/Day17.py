
from utils import Input, printResult

# https://adventofcode.com/2021/day/17

x1, x2, y1, y2 = 20, 30, -10, -5
x1, x2, y1, y2 = 241, 275, -75, -49

m, n = 0, 0

def check (x1, x2, y1, y2, dx, dy):
    x, y = 0, 0
    global n, m
    maxY = 0
    for _ in range(10000):
        x += dx
        y += dy
        maxY = max(y, maxY)
        if y > maxY:
            maxY = y
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            m = max(m, maxY)
            n += 1
            return True
        if x > x2 or y < y1:
            break
        if dx > 0:
            dx -= 1
        dy -= 1
    return False
    
for dx in range(0, 300):
    for dy in range(-100, 100):
        check(x1, x2, y1, y2, dx, dy)

# check(x1, x2, y1, y2, 6, 3)

printResult(1, m)
printResult(2, n)
