
from utils import Input, printResult

# https://adventofcode.com/2022/day/3

input = Input(2022, 3).lines()

res = 0
for s in input:
    n = len(s) // 2
    c = (set(s[:n]) & set(s[n:])).pop()
    res += (ord(c) - ord('A') + 27) if c < 'a' else (ord(c) - ord('a') + 1)

printResult(1, res)

res = 0
for i in range(len(input) // 3):
    s1, s2, s3 = input[i*3:i*3+3]
    c = (set(s1) & set(s2) & set(s3)).pop()
    res += (ord(c) - ord('A') + 27) if c < 'a' else (ord(c) - ord('a') + 1)

printResult(2, res)
