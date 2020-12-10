
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/5

input = Input(2020, 5).lines()
seats = set(int(re.sub("B|R", "1", re.sub('F|L', '0', line)), 2) for line in input)

printResult(1, max(seats))
printResult(2, min(x+1 for x in seats if x+1 not in seats))
