
from utils import Input, printResult

# https://adventofcode.com/2022/day/7

input = list(Input(2022, 7).lines())

fs = {'/': {}}
cur = fs
path = []
i = 0
while i < len(input):
    s = input[i]
    if s.startswith("$ cd"):
        d = s[5:]
        if d == '..':
            path.pop()
        elif d == '/':
            path = ['/']
        else:
            path.append(d)
        cur = fs
        for p in path:
            cur = cur[p]
        i += 1
    elif s == '$ ls':
        i += 1
        while i < len(input) and not input[i].startswith('$'):
            s = input[i].split(' ')
            if s[0] == 'dir':
                cur[s[1]] = {}
            else:
                cur[s[1]] = int(s[0])
            i += 1
    else:
        raise Exception('invalid input')
    
def count_size(path, fs):
    size = 0
    for f in fs:
        if type(fs[f]) == int:
            size += fs[f]
        else:
            size += count_size(path + '/' + f, fs[f])
    sizes[path] = size
    return size

sizes = {}
count_size("", fs)
printResult(1, sum(s for s in sizes.values() if s < 100_000))

needspace = sizes[''] - 40_000_000
printResult(2, next(x for x in sorted(sizes.values()) if x > needspace))
