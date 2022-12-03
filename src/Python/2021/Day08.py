
from utils import Input, printResult
import itertools

# https://adventofcode.com/2021/day/8

input = Input(2021, 8).lines()

digits = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf",
    "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
]

n1, n2 = 0, 0
for s in input:
    left, right = s.split(" | ")
    nums = list(map(set, sorted(left.split(), key = len)))
    a = (nums[1] - nums[0]).pop()
    d = (nums[3] & nums[4] & nums[5] & nums[2]).pop()
    b = (nums[2] - nums[0] - set(d)).pop()
    g = (nums[3] & nums[4] & nums[5] - set([a, d])).pop()
    f = (nums[0] & nums[6] & nums[7] & nums[8]).pop()
    c = (nums[0] - set(f)).pop()
    e = (set("abcdefg") - set([a, b, c, d, f, g])).pop()
    subs = [a, b, c, d, e, f, g]
    for i, n in enumerate(right.split()):
        n = "".join(sorted(chr(ord('a') + subs.index(c)) for c in n))
        n = digits.index(n)
        n1 += n in [1, 4, 7, 8]
        n2 += n * (10 ** (3-i))

printResult(1, n1)
printResult(2, n2)
