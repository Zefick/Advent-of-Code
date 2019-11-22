
from utils import Input, printResult
import copy

# https://adventofcode.com/2018/day/7

pattern = "Step (.) must be finished before step (.) can begin."
steps = set()
order = {}
for m in Input(2018, 7).match(pattern):
    s1, s2 = m[1], m[2]
    steps.add(s1)
    steps.add(s2)
    if s2 not in order:
        order[s2] = []
    order[s2].append(s1)
steps = list(sorted(steps))

def simulate(order, steps, n):
    time, sequence = 0, ""
    workers = [0] * n
    letters = [None] * n
    while len(order) != 0:
        time += 1
        for i in range(n):
            workers[i] = max(0, workers[i] - 1)
            if workers[i] == 0:
                if letters[i]:
                    l = letters[i]
                    for list in order.values():
                        if l in list: list.remove(l)
                    order.pop(l, None)
                    letters[i] = None
                x = next(filter(lambda s: s not in order or len(order[s]) == 0, steps), None)
                if x:
                    steps.remove(x)
                    sequence += x
                    workers[i] = ord(x) - ord('A') + 61
                    letters[i] = x
            
    return (time - 1, sequence)

printResult(1, simulate(copy.deepcopy(order), list(steps), 1)[1])
printResult(2, simulate(copy.deepcopy(order), list(steps), 5)[0])
