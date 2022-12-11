
from utils import Input, printResult

# https://adventofcode.com/2022/day/8

input = Input(2022, 8).lines()

n = len(input)
m = len(input[0])

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0
best = None
for i in range(n):
    for j in range (m):
        h = int(input[i][j])
        
        # part1
        for dx, dy in dirs:
            x, y = i+dx, j+dy
            while x >= 0 and y >= 0 and x < n and y < m:
                if int(input[x][y]) < h:
                    x += dx
                    y += dy
                else:
                    break
            else:
                ans += 1
                break
        
        # part 2
        cur_x = 1
        for dx, dy in dirs:
            view = 0
            x, y = i + dx, j + dy
            h2 = 0
            while x >= 0 and y >= 0 and x < n and y < m:
                view += 1
                if int(input[x][y]) >= h:
                    break
                x += dx
                y += dy
            cur_x *= view
        if best is None or cur_x > best:
            best = cur_x

printResult(1, ans)
printResult(2, best)
