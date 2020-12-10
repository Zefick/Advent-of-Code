
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/7

input = Input(2020, 7).match("(.+?) bags contain (.*)")

contents = {}
pattern = re.compile("(\\d+) (.+) bag(s)?")

for m in input:
    if m[2] != "no other bags.":
        bags = m[2].split(", ")
        arr = []
        for b in bags:
            m2 = pattern.match(b)
            arr.append((int(m2[1]), m2[2]))
        contents[m[1]] = arr

contents2 = {}
for k, v in contents.items():
    for _, bag in v:
        if bag not in contents2:
            contents2[bag] = set()
        contents2[bag].add(k)

def countPart1(bag):
    if bag not in contents2:
        return []
    else:
        result = list(contents2[bag])
        for x in contents2[bag]:
            result += countPart1(x)
        return result

def countPart2(bag):
    n = 1
    if bag in contents:
        for num, bags in contents[bag]:
            n += num * countPart2(bags)
    return n

start = "shiny gold"
printResult(1, len(set(countPart1(start))))
printResult(2, countPart2(start) - 1)
