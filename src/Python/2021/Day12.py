
from collections import defaultdict
from utils import Input, printResult
from functools import lru_cache

# https://adventofcode.com/2021/day/12

input = Input(2021, 12).lines()

edges = defaultdict(set)
for s in input:
    a, b = s.split('-')
    edges[a].add(b)
    edges[b].add(a)

@lru_cache(maxsize=None)
def visit(start, visited, allowed):
    n = 0
    for node in edges[start]:
        if node == 'end':
            n += allowed is None
        elif node.isupper() or node not in visited:
            n += visit(node, frozenset(visited | {node}), allowed)
        elif node == allowed:
            n += visit(node, visited, None)
    return n

n = visit('start', frozenset({'start'}), None)
printResult(1, n)

for e in edges.keys():
    if e.islower() and e not in['start', 'end']:
        n += visit("start", frozenset({'start'}), e)

printResult(2, n)
