
from utils import Input, printResult

# https://adventofcode.com/2022/day/2

input = Input(2022, 2).lines()

score1, score2 = 0, 0
for s in input:
    a = ord(s[0]) - ord('A')
    b = ord(s[2]) - ord('X')
    score1 += 1 + b + (3 if a == b else 6 if (a + 1) % 3 == b else 0)
    score2 += 1 + 3 * b + (a if b == 1 else (a-1) % 3 if b == 0 else (a+1) % 3)
printResult(1, score1)

printResult(2, score2)
