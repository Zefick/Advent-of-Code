
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/18

input = Input(2020, 18).lines()
input = [s.replace(" ", "") for s in input]

# expr   :: term (+|* term)*
# term   :: int | (expr)

def term1(input):
    val = input.pop(0)
    if val == '(':
        val = expr1(input)
        input.pop(0)
    return int(val)

def expr1(input):
    result = term1(input)
    while input and input[0] in ['*', '+']:
        op = int.__add__ if input[0] == '+' else int.__mul__
        input.pop(0)
        result = op(result, term1(input))
    return result

# expr   :: term (* term)*
# term   :: factor (+ factor)*
# factor :: int | (expr)

def factor2(input):
    val = input.pop(0)
    if val == '(':
        val = expr2(input)
        input.pop(0)
    return int(val)

def term2(input):
    result = factor2(input)
    while input and input[0] == '+':
        input.pop(0)
        result += factor2(input)
    return result

def expr2(input):
    result = term2(input)
    while input and input[0] == '*':
        input.pop(0)
        result *= term2(input)
    return result

printResult(1, sum(map(expr1, map(list, input))))
printResult(2, sum(map(expr2, map(list, input))))
