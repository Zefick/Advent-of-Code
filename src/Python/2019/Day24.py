
import math
from utils import Input, printResult
import copy

# https://adventofcode.com/2019/day/24

def step1(grid):
    nextGrid = []
    for i in range(25):
        n = 0
        if i > 4: n += grid[i-5] == '#'
        if i % 5 > 0: n += grid[i-1] == '#'
        if i % 5 < 4: n += grid[i+1] == '#'
        if i < 20: n += grid[i+5] == '#'
        nextGrid.append(['.','#'][n == 1 or (grid[i] == '.' and n == 2)])
    return "".join(nextGrid)

visited = set()
input = ".##..##.#.##.##.#..##.###"
while input not in visited:
    visited.add(input)
    input = step1(input)
b = sum(2 ** i if input[i] == '#' else 0 for i in range(25))
printResult(1, b)

# part 2

def step2(grid):
    newGrid = {}
    minLevel = min(grid.keys())
    maxLevel = max(grid.keys())
    for l in range(minLevel-1, maxLevel + 2):
        level = [0] * 25
        for i in range(25):
            n = 0
            current = '.'
            if l >= minLevel and l <= maxLevel:
                current = grid[l][i]
                if i > 4:     n += grid[l][i-5] == '#'
                if i % 5 > 0: n += grid[l][i-1] == '#'
                if i % 5 < 4: n += grid[l][i+1] == '#'
                if i < 20:    n += grid[l][i+5] == '#'
            if l < maxLevel:
                if i < 5:      n += grid[l+1][7]  == '#'
                if i % 5 == 0: n += grid[l+1][11] == '#'
                if i % 5 == 4: n += grid[l+1][13] == '#'
                if i > 19:     n += grid[l+1][17] == '#'
            if l > minLevel:
                if i == 7:  n += sum(grid[l-1][j] == '#' for j in range(5))
                if i == 11: n += sum(grid[l-1][j] == '#' for j in range(0, 25, 5))
                if i == 13: n += sum(grid[l-1][j] == '#' for j in range(4, 25, 5))
                if i == 17: n += sum(grid[l-1][j] == '#' for j in range(20, 25))
            level[i] = ['.','#'][n == 1 or (current == '.' and n == 2)]
        if l != minLevel-1 and l != maxLevel+1 or level.count('#') > 0:
            level[12] = '?'
            newGrid[l] = "".join(level)
    return newGrid

import time
t = time.time()

grid = {0: ".##..##.#.##?##.#..##.###"}
for i in range(200):
    grid = step2(grid)

printResult(2, sum(map(lambda s: s.count('#'), grid.values())))
print("%.2f" % (time.time() - t))
