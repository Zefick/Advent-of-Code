
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/4

input = Input(2020, 4).lines()
input.append("")

ecls = set(['amb','blu','brn','gry','grn','hzl','oth'])

def check(fields) :
    val = int(fields['byr'])
    if val < 1920 or val > 2002:
        return False
    val = int(fields['iyr'])
    if val < 2010 or val > 2020:
        return False
    val = int(fields['eyr'])
    if val < 2020 or val > 2030:
        return False
    m = re.match('(\\d+)(cm|in)$', fields['hgt'])
    if m:
        h = int(m[1])
        if not ((m[2] == 'cm' and h >= 150 and h <= 193) or
                (m[2] == 'in' and h >= 59 and h <= 76)):
            return False
    else:
        return False
    return re.match("#[a-f0-9]{6}$", fields['hcl']) \
        and fields['ecl'] in ecls \
        and re.match("\\d{9}$", fields['pid'])

part1, part2 = 0, 0
fields = {}
for line in input:
    if len(line) == 0:
        if len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields):
            part1 += 1
            if check(fields):
                part2 += 1
        fields = {}
    else:
        for part in line.split():
            p = part.split(":")
            fields[p[0]] = p[1]
                
printResult(1, part1)
printResult(2, part2)
