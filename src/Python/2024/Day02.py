
from utils import Input, printResult

# https://adventofcode.com/2024/day/2

input = Input(2024, 2).lines()

def is_safe(nums):
    if nums != sorted(nums) and nums != sorted(nums)[::-1]:
        return False
    if all(1 <= abs(nums[i+1]-nums[i]) <= 3 for i in range(len(nums)-1)):
        return True
    return False

part1, part2 = 0, 0
for line in input:
    nums = list(map(int, line.split()))
    if (is_safe(nums)):
        part1 += 1
        part2 += 1
        continue
    safe = False
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            part2 += 1
            safe = True
            break

printResult(1, part1)
printResult(2, part2)
