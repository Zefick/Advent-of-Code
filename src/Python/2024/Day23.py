
from utils import Input, printResult
from collections import defaultdict
from itertools import combinations

# https://adventofcode.com/2024/day/23

input = Input(2024, 23).lines()

graph = defaultdict(set)
comps = set()
for line in input:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)
    comps.add(a)
    comps.add(b)

part1 = set()
longest_lan = []
for c1 in comps:
    if c1[0] == 't':
        for c2, c3 in combinations(graph[c1], 2):
            if c3 in graph[c2]:
                part1.add(tuple(sorted([c1, c2, c3])))
    lan = set([c1])
    for c2 in comps:
        if lan.issubset(graph[c2]):
            lan.add(c2)
    if len(lan) > len(longest_lan):
        longest_lan = lan

printResult(1, len(part1))
printResult(2, ",".join(sorted(longest_lan)))
