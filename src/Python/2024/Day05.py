
from utils import Input, printResult
from collections import defaultdict
from itertools import combinations

# https://adventofcode.com/2024/day/5

input = Input(2024, 5).lines()

rules = defaultdict(list)
pages = []

for line in input:
    if line.count('|'):
        a, b = line.split('|')
        rules[a].append(b)
    elif line:
        pages.append(line.split(","))

def isCorrect(page):
    return all(c2 in rules[c1] for c1, c2 in combinations(page, 2))

part1 = 0
part2 = 0
for page in pages:
    if isCorrect(page):
        part1 += int(page[len(page) // 2])
    else:
        correct_page = []
        nums = set(page)
        # we only need to fill the half or the page
        # the rest could be corrected but irrelevant
        for _ in range(len(page) // 2 + 1):
            for n in nums:
                if all(n==m or m in rules[n] for m in nums):
                    correct_page.append(n)
                    nums.remove(n)
                    break
        part2 += int(correct_page[-1])

printResult(1, part1)
printResult(2, part2)
