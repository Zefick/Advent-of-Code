
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/7

input = list(map(int, Input(2019, 7).lines()[0].split(",")))

#art 1
import itertools
results = []
for p in list(itertools.permutations(range(5))):
    output = 0
    for x in p:
        output = next(Intcode(input).run([x, output]))
    results.append(output)
printResult(1, max(results))

# part 2
results = []
for p in list(itertools.permutations(range(5, 10))):
    queues = [[p[0], 0], [p[1]], [p[2]], [p[3]], [p[4]]]
    amps = list(Intcode(input).run(queues[i]) for i in range(5))
    i = 0
    while True:
        x = next(amps[i], None)
        if x is not None and x != "wait":
            queues[(i + 1) % 5].append(x)
        if x is None and i == 4:
            break
        i = (i + 1) % 5
    results.append(queues[0][-1])

printResult(2, max(results))
