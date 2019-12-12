
from utils import Input, printResult

# https://adventofcode.com/2019/day/8

input = list(map(int, Input(2019, 8).lines()[0]))

W, H = 25, 6
n = len(input) // (W * H)

minIndex = min(range(n),
        key = lambda i: input[i * W * H: (i+1) * W * H].count(0))
layer = input[minIndex * W * H: (minIndex+1) * W * H]
printResult(1, layer.count(1) * layer.count(2))

image = ""
palette = {0: "  ", 1: "@@"}
for y in range(H):
    image += "\n" + "".join(
        palette[next(filter(lambda p: p != 2, input[W * y + x :: W * H]))]
        for x in range(W))

printResult(2, image)
