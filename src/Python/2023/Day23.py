
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2023/day/23

input = Input(2023, 23).lines()

w, h = len(input[0]), len(input)

def neigthbors1(y: int, x: int):
    dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for dy, dx in dirs:
        y2, x2 = y + dy, x + dx
        if 0 <= y2 < h and 0 <= x2 < w:
            if input[y2][x2] == '.' \
                    or (dx == -1 and input[y2][x2] == '<') or (dx == 1 and input[y2][x2] == '>') \
                    or (dy == -1 and input[y2][x2] == '^') or (dy == 1 and input[y2][x2] == 'v'):
                yield(y2, x2)
  
# Iterative approach using programming stack to avoid stack overflow.
# This function traverses the input map without reducing the graph since it is quite fast in part 1.
# (reducing would take the same time by itself)
def hike1():
    q = [(1, 0, 1, 0)]
    path = set()
    l = 0
    m = 0
    while q:
        x, y, ch, l = q.pop()
        if ch == 1:
            q.append((x, y, 0, l))
            path.add((x, y))
        else:
            path.remove((x, y))
            continue
        for y2, x2 in neigthbors1(y, x):
            if y2 == h-1:
                m = max(m, l + 1)
            elif (x2, y2) not in path:
                q.append((x2, y2, 1, l + 1))
    return m

printResult(1, hike1())

# PART II

def neigthbors2(y: int, x: int):
    dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for dy, dx in dirs:
        y2, x2 = y + dy, x + dx
        if 0 <= y2 < h and 0 <= x2 < w:
            if input[y2][x2] != '#':
                yield(y2, x2)

# reduction of the map by replacing every straigth section with an edge in the result graph.
def build_graph(cur, prev, last, graph):
    steps = 1
    while True:
        if cur in graph and last in graph[cur]:
            return
        y, x = cur
        nbs = list(neigthbors2(y, x))
        if len(nbs) > 2 or (y, x) == (h-1, w-2):
            graph[last][(y, x)] = steps
            graph[(y, x)][last] = steps
            for y2, x2 in nbs:
                if (y2, x2) != prev:
                    build_graph((y2, x2), (y, x), (y, x), graph)
            break
        for y2, x2 in nbs:
            if (y2, x2) != prev:
                cur = (y2, x2)
                prev = (y, x)
                steps += 1
                break

cnt = 0
def hike2(node, path):
    global cnt
    cnt += 1
    m = 0
    path[node] = 1
    for node2, pts in graph[node]:
        if node2 == len(graph)-1:
            m = pts
        elif path[node2] == 0:
            l = hike2(node2, path)
            if l > 0:
                m = max(m, pts + l)
    path[node] = 0
    return m

import time
t = time.time()

graph = defaultdict(dict)
build_graph((0, 1), None, (0, 1), graph)
nodes = list(graph.keys())
graph = [[(nodes.index(edge), pts) for edge, pts in edges.items()] for edges in graph.values()]

printResult(2, hike2(0, [0] * len(graph)) - 1)

print(cnt)
print(time.time() - t)