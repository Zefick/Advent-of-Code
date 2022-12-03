
from utils import Input, printResult

# https://adventofcode.com/2021/day/18

input = Input(2021, 18).lines()

def parse(data: str) -> list :
    stack = []
    for c in data:
        if c.isdigit():
            stack.append([int(c)])
        elif c == ']':
            r = stack.pop()
            l = stack.pop()
            stack.append([l, r])
    return stack.pop()

def last(node, idx):
    while len(node) > 1:
        node = node[idx]
    return node

def explode(node, depth, left, right):
    if len(node) == 2:
        if depth == 4:
            if left:
                last(left, 1)[0] += node[0][0]
            if right:
                last(right, 0)[0] += node[1][0]
            node[0] = 0
            node.pop()
        else:
            explode(node[0], depth+1, left, node[1])
            explode(node[1], depth+1, node[0], right)

def split(node):
    if len(node) == 2:
        return split(node[0]) or split(node[1])
    elif node[0] > 9:
        node.append([node[0] // 2 + node[0] % 2])
        node[0] = [node[0] // 2]
        return True
    return False

def reduce(tree):
    while True:
        explode(tree, 0, None, None)
        if not split(tree):
            break
    return tree

def magnitude(pair) :
    a = pair[0][0] if len(pair[0]) == 1 else magnitude(pair[0])
    b = pair[1][0] if len(pair[1]) == 1 else magnitude(pair[1])
    return a * 3 + b * 2

pair = parse(input[0])
for pair2 in input[1:]:
    pair = reduce([pair, parse(pair2)])

printResult(1, magnitude(pair))

import time
t = time.time()

m = 0
for a in input:
    for b in input:
        if a != b:
            mag = magnitude(reduce([parse(a), parse(b)]))
            m = max(m, mag)

printResult(2, m)

print(time.time() - t)
