
from utils import Input, printResult
import heapq

# https://adventofcode.com/2021/day/15

input = Input(2021, 15).lines()
input = list(list(map(int, input[i])) for i in range(len(input)))

def search(map):
    n = 0
    w = len(map[0])
    h = len(map)
    lowest = list([10000] * w for _ in range(h))
    steps = [(0, 0, 0)]
    while len(steps) > 0:
        n += 1
        (dist, x, y) = heapq.heappop(steps)
        for x2, y2 in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if x2 >= 0 and x2 < w and y2 >=0 and y2 < h:
                val = dist + map[x2][y2]
                if lowest[x2][y2] > val:
                    lowest[x2][y2] = val
                    heapq.heappush(steps, (val, x2, y2))
    return lowest[-1][-1]

printResult(1, search(input))

w = len(input[0])
h = len(input)
input2 = list([0] * w * 5 for _ in range(h * 5))
for y in range(h*5):
    for x in range(w*5):
        input2[y][x] = (input[y%h][x%w] + (x // w) + (y // h) -1) % 9 + 1

printResult(2, search(input2))
