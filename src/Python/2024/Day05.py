
from utils import Input, printResult
from itertools import combinations

# https://adventofcode.com/2024/day/5

input = Input(2024, 5).lines()

rules = set()
pages = []

for line in input:
    if '|' in line:
        rules.add(tuple(line.split('|')))
    elif line:
        pages.append(line.split(","))

def isCorrect(page):
    return all((c1, c2) in rules for c1, c2 in combinations(page, 2))

part1 = 0
part2 = 0
for page in pages:
    if isCorrect(page):
        part1 += int(page[len(page) // 2])
    else:
        nums = set(page)
        page = []
        # we only need to fill the half or the page
        # the rest could be corrected but irrelevant
        for _ in range(len(page) // 2 + 1):
            for n in nums:
                if all(n==m or (n, m) in rules for m in nums):
                    page.append(n)
                    nums.remove(n)
                    break
        part2 += int(page[-1])

printResult(1, part1)
printResult(2, part2)
