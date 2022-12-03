
from utils import Input, printResult

# https://adventofcode.com/2021/day/10

input = Input(2021, 10).lines()

points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

pts1, pts2 = 0, []
for s in input:
    stack = []
    for c in s:
        if c in ")]}>":
            if stack[-1] == pairs[c]:
                stack.pop()
            else:
                pts1 += points1[c]
                break
        else:
            stack.append(c)
    else:
        score = 0
        for c in stack[::-1]:
            score = score * 5 + points2[c]
        pts2.append(score)

printResult(1, pts1)

pts2 = sorted(pts2)

printResult(2, pts2[len(pts2) // 2])
