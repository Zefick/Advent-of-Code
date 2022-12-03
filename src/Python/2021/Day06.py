
from utils import Input, printResult

# https://adventofcode.com/2021/day/6

input = list(map(int, Input(2021, 6).lines()[0].split(",")))

# input = [3,4,3,1,2]

nums = {x: input.count(x) for x in range(9)}

for i in range(256):
    next_nums = {x: nums[(x+1)%9] for x in range(9)}
    next_nums[6] += next_nums[8]
    nums = next_nums
    if i == 80:
        printResult(1, sum(nums.values()))

printResult(2, sum(nums.values()))
