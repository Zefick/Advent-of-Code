
from utils import Input, printResult
from functools import cache
from time import time

# https://adventofcode.com/2022/day/16

input = Input(2022, 16).match("Valve (..) has flow rate=(\d+); .* valves? (.*)")

graph = {}
for m in input:
    valve = m[1]
    rate = int(m[2])
    out = m[3].split(', ')
    graph[valve] = (rate, out)

def calc_pressure(opened):
    return sum(graph[x][0] for x in opened)

# initial solution
# quite fast but slower then optimized BFS

@cache
def dfs1(cur, time, opened):
    p = calc_pressure(opened)
    best = 0
    if time < 29:
        if cur not in opened and graph[cur][0] > 0:
            best = dfs1(cur, time + 1, frozenset(opened | set([cur])))
        for next in graph[cur][1]:
            best = max(best, dfs1(next, time + 1, opened))
    return p + best

# optimized part 1
# finds a solution 100x faster
# BFS with cutting off bad variants (score < maximum - 100)

def bfs1():
    positions = {("AA", frozenset()): 0}
    for time in range(30):
        m = max(positions.values())
        next_positions = {}
        for (cur, opened), p in positions.items():
            if p < m - 100:
                continue
            candidates = set()
            p += calc_pressure(opened)
            # open
            if (cur not in opened) and graph[cur][0] > 0:
                candidates.add((cur, frozenset(opened | set([cur]))))
            # move
            for next in graph[cur][1]:
                candidates.add((next, opened))
            for pos2 in candidates:
                if pos2 not in next_positions or next_positions[pos2] < p:
                    next_positions[pos2] = p
        positions = next_positions
        # print(time, len(next_positions), min(positions.values()), max(positions.values()))
    return max(positions.values())
            
t = time()
# best = dfs1('AA', 0, frozenset())
best = bfs1()
printResult(1, best, time() - t)

# Same approach as in BFS for part 1 but now it tracks two valves at a time

def bfs2():
    positions = {("AA", "AA", frozenset()): 0}
    for time in range(26):
        m = max(positions.values())
        next_positions = {}
        for (cur1, cur2, opened), p in positions.items():
            if p < m - 100:
                continue
            candidates = set()
            p += calc_pressure(opened)
            if cur1 not in opened and graph[cur1][0] > 0:
                # open + open
                if cur2 != cur1 and (cur2 not in opened) and graph[cur2][0] > 0:
                    candidates.add((cur1, cur2, frozenset(opened | set([cur1, cur2]))))
                # open + move
                for next2 in graph[cur2][1]:
                    candidates.add((cur1, next2, frozenset(opened | set([cur1]))))
            for next1 in graph[cur1][1]:
                # move + open
                if (cur2 not in opened) and graph[cur2][0] > 0:
                    candidates.add((next1, cur2, frozenset(opened | set([cur2]))))
                # move + move
                for next2 in graph[cur2][1]:
                    candidates.add((next1, next2, opened))
            for v1, v2, opened in candidates:
                pos2 = min(v1, v2), max(v1, v2), opened
                if pos2 not in next_positions or next_positions[pos2] < p:
                    next_positions[pos2] = p
        positions = next_positions
        # print(time, len(next_positions), min(positions.values()), max(positions.values()))
    return max(positions.values())

t = time()
best = bfs2()
printResult(2, best, time() - t)
