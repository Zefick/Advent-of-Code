
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/16

input = Input(2020, 16).lines()

p1 = re.compile("(.*): (\\d+)-(\\d+) or (\\d+)-(\\d+)")

fields = {}
for i in range(len(input)):
    if len(input[i]) == 0:
        break
    m = p1.match(input[i])
    fields[m[1]] = [[int(m[2]), int(m[3])], [int(m[4]), int(m[5])]]

my_ticket = list(map(int, input[i+2].split(',')))

def suitable(val, ranges):
    return (val >= ranges[0][0] and val <= ranges[0][1]) \
        or (val >= ranges[1][0] and val <= ranges[1][1])

i += 5
invalid = []
tickets = []
for ticket in input[i:]:
    fs = list(map(int, ticket.split(',')))
    valid = True
    for f in fs:
        if not any(suitable(f, ranges) for ranges in fields.values()):
            valid = False
            invalid.append(f)
    if valid:
        tickets.append(fs)

printResult(1, sum(invalid))

for f, ranges in fields.items():
    fields[f] = list(i for i in range(len(fields)) if all(suitable(t[i], ranges) for t in tickets))

while True:
    single = [fields[f][0] for f in fields if len(fields[f]) == 1]
    if len(single) == len(fields):
        break
    for s in single:
        for f in fields:
            if len(fields[f]) > 1 and s in fields[f]:
                fields[f].remove(s)

my_ticket = [my_ticket[fields[f][0]] for f in fields if f.startswith("departure")]
printResult(2, my_ticket[0] * my_ticket[1] * my_ticket[2] * my_ticket[3] * my_ticket[4] * my_ticket[5])
