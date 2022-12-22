
from utils import Input, printResult

# https://adventofcode.com/2022/day/12

input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

input = Input(2022, 12).lines()
input = list(map(list, input))

n = len(input)
m = len(input[0])

for i in range(n):
    for j in range(m):
        if input[i][j] == 'E':
            E = (i, j)
            input[i][j] = 'z'
        if input[i][j] == 'S':
            S = (i, j)
            input[i][j] = 'a'
            
dirs = [[-1, 0], [1, 0], [0, 1], [0,-1]]

def find_path(i, j):
    steps = 0
    visited = set()
    cur = [(i, j)]
    while cur:
        next_moves = set()
        for y, x in cur:
            h = ord(input[y][x])
            for dy, dx in dirs:
                x2, y2 = x + dx, y + dy
                if (0 <= x2 < m) and (0 <= y2 < n) and \
                        ord(input[y2][x2]) - h <= 1 and (y2, x2) not in visited:
                    if (y2, x2) == E:
                        return steps + 1
                    next_moves.add((y2, x2))
                    visited.add((y2, x2))
        cur = next_moves
        steps += 1
    return float('inf')
        
best = find_path(*S)
printResult(1, best)

for i in range(n):
    for j in range(m):
        if input[i][j] == 'a':
            best = min(best, find_path(i, j))
        
printResult(2, best)
