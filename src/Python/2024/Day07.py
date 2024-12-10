
from utils import Input, printResult

# https://adventofcode.com/2024/day/7

input = Input(2024, 7).lines()

def check1(target, nums, acc, i):
    if i == len(nums):
        return target == acc
    return check1(target, nums, acc + nums[i], i+1) or \
        check1(target, nums, acc * nums[i], i+1)
        
def concat(x, y):
    m = 1
    while y >= m:
        m *= 10
    return x * m + y     

def check2(target, nums, acc, i):
    if acc > target:
        return False
    if i == len(nums):
        return target == acc
    return check2(target, nums, acc + nums[i], i+1) or \
        check2(target, nums, acc * nums[i], i+1) or \
        check2(target, nums, concat(acc, nums[i]), i+1)

part1, part2 = 0, 0
for line in input:
    line = line.split(": ")
    left = int(line[0])
    right = list(map(int, line[1].split()))
    if check1(left, right, right[0], 1):
        part1 += left
    if check2(left, right, right[0], 1):
        part2 += left

printResult(1, part1)
printResult(2, part2)
