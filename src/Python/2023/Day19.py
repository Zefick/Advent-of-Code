
from utils import Input, printResult
from functools import reduce

# https://adventofcode.com/2023/day/19

input = list(Input(2023, 19).match("((\w+)\{(.*),(\w+)\})|(\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\})"))

rules = {}
details = []

for m in input:
    if m:
        if m[1]:
            rules[m[2]] = (m[3].split(','), m[4])
        else:
            details.append((int(m[6]), int(m[7]), int(m[8]), int(m[9])))

res = 0
for d in details:
    wf = 'in'
    while wf not in ['R', 'A']:
        for part in rules[wf][0]:
            rule, dst = part.split(':')
            i = "xmas".index(rule[0])
            op = rule[1]
            n = int(rule[2:])
            if (op == '<' and d[i] < n) or (op == '>' and d[i] > n):
                wf = dst
                break
        else:
            wf = rules[wf][1]
    if wf == 'A':
       res += sum(d) 

printResult(1, res)

def check(workflow, combinations):
    if workflow == 'R':
        return 0
    if workflow == 'A':
        lens = (c[1] - c[0] + 1 for c in combinations)
        return reduce(int.__mul__, lens, 1)
    res = 0
    for part in rules[workflow][0]:
        rule, dst = part.split(':')
        i = "xmas".index(rule[0])
        op = rule[1]
        n = int(rule[2:])
        left, right = list(combinations), list(combinations)
        r = combinations[i]
        if op == '<':
            left[i] = (r[0], n-1)
            right[i] = (n, r[1])
        else:
            left[i] = (n+1, r[1])
            right[i] = (r[0], n)
            
        res += check(dst, left)
        combinations = right
    res += check(rules[workflow][1], combinations)
    return res

printResult(2, check('in', ((1, 4000), (1, 4000), (1, 4000), (1, 4000))))
