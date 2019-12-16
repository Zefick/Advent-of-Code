
from utils import Input, printResult

# https://adventofcode.com/2019/day/9

from intcode import Intcode
input = list(map(int, Input(2019, 9).lines()[0].split(",")))

printResult(1, next(Intcode(input, [1]).run()))
printResult(2, next(Intcode(input, [2]).run()))
