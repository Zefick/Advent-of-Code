
from utils import Input, printResult

# https://adventofcode.com/2022/day/25

input = Input(2022, 25).lines()

digits = {'0': 0, '1':1, '2': 2, '-':-1, '=':-2} 

def convert1(s):
    res = 0
    mul = 1
    for c in s[::-1]:
        x = digits[c]
        res += mul * x
        mul *= 5
    return res

def convert2(n):
    res = ""
    while n > 0:
        n, rem = divmod(n, 5)
        if rem >= 3:
            res += '=' if rem == 3 else '-'
            n += 1
        else:
            res += str(rem)
    return res[::-1]

n = sum(convert1(s) for s in input)

printResult(1, convert2(n))
